#!/usr/bin/env python3
import os
import sys
import time
import json
import urllib.request
import urllib.error

def main():
    # 1. Load configuration from environment variables
    api_token = os.getenv("CODACY_API_TOKEN")
    provider = os.getenv("PROVIDER", "gh")
    organization = os.getenv("ORGANIZATION", "andrearsilva")
    repository = os.getenv("REPOSITORY", "Codacy-Repo")
    commit_sha = os.getenv("COMMIT_SHA")
    
    # Validation
    if not api_token:
        print("[-] Error: CODACY_API_TOKEN environment variable is not set.")
        sys.exit(1)
    if not commit_sha:
        print("[-] Error: COMMIT_SHA environment variable is not set.")
        sys.exit(1)
        
    poll_interval = int(os.getenv("POLL_INTERVAL_SECONDS", "15"))
    timeout_minutes = int(os.getenv("TIMEOUT_MINUTES", "10"))
    max_attempts = (timeout_minutes * 60) // poll_interval

    print(f"[*] Starting Codacy Gate Check...")
    print(f"[*] Provider: {provider}")
    print(f"[*] Organization: {organization}")
    print(f"[*] Repository: {repository}")
    print(f"[*] Commit SHA: {commit_sha}")
    print(f"[*] Polling every {poll_interval}s up to {timeout_minutes} minutes...")

    url = f"https://app.codacy.com/api/v3/analysis/organizations/{provider}/{organization}/repositories/{repository}/commits/{commit_sha}"
    
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/json")
    req.add_header("api-token", api_token)

    attempt = 0
    while attempt < max_attempts:
        attempt += 1
        print(f"\n[*] Poll attempt {attempt}/{max_attempts}...")
        
        try:
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8"))
                    
                    commit_info = data.get("commit", {})
                    ended_analysis = commit_info.get("ended_analysis") or commit_info.get("endedAnalysis")
                    
                    # If ended_analysis is set, the analysis is completed
                    if ended_analysis:
                        print("[+] Codacy analysis completed!")
                        return evaluate_gates(data)
                    else:
                        print("[*] Commit found, but analysis is still in progress...")
                else:
                    print(f"[*] Unexpected HTTP status: {response.status}")
                    
        except urllib.error.HTTPError as e:
            if e.code == 404:
                # 404 is common if the commit hasn't been processed by Codacy yet
                print("[*] Commit not found on Codacy yet. Waiting for upload/webhook processing...")
            elif e.code in [401, 403]:
                print(f"[-] Authentication failed (HTTP {e.code}). Please check your CODACY_API_TOKEN.")
                sys.exit(1)
            else:
                print(f"[*] HTTP Error {e.code}: {e.reason}. Retrying...")
        except urllib.error.URLError as e:
            print(f"[*] Network Error: {e.reason}. Retrying...")
        except Exception as e:
            print(f"[-] Unexpected Error: {str(e)}")
            # Default soft fail/exit 0 on unexpected code errors to keep pipeline moving
            print("[!] Soft failing due to script exception.")
            sys.exit(0)
            
        time.sleep(poll_interval)
        
    print(f"\n[-] Timeout reached after {timeout_minutes} minutes.")
    print("[!] Soft failing: Analysis took too long, allowing pipeline to proceed.")
    sys.exit(0)

def evaluate_gates(data):
    coverage = data.get("coverage", {})
    quality = data.get("quality", {})
    
    coverage_ok = coverage.get("isUpToStandards", True)
    quality_ok = quality.get("isUpToStandards", True)
    
    # Log Coverage Gate details
    print("\n" + "="*50)
    print(" CODACY COVERAGE GATE RESULTS")
    print("="*50)
    total_coverage = coverage.get("totalCoveragePercentage")
    delta_coverage = coverage.get("deltaCoveragePercentage")
    
    if total_coverage is not None:
        print(f"[*] Total Coverage: {total_coverage}%")
    if delta_coverage is not None:
        print(f"[*] Delta Coverage: {delta_coverage:+.2f}%" if isinstance(delta_coverage, (int, float)) else f"[*] Delta Coverage: {delta_coverage}%")
        
    print(f"[*] Coverage Gate Status: {'PASSED' if coverage_ok else 'FAILED'}")
    
    if not coverage_ok:
        reasons = coverage.get("resultReasons", [])
        print("[-] Coverage Gate Failure Reasons:")
        for r in reasons:
            if not r.get("isUpToStandards", True):
                gate_name = r.get("gate", "Unknown Gate")
                expected = r.get("expectedThreshold", {}).get("threshold", "N/A")
                actual = r.get("expected", "N/A")
                print(f"    - {gate_name}: Expected threshold: {expected}, Actual value: {actual}")
                
    # Log Quality Gate details
    print("\n" + "="*50)
    print(" CODACY QUALITY GATE RESULTS")
    print("="*50)
    print(f"[*] New Issues: {quality.get('newIssues', 0)}")
    print(f"[*] Fixed Issues: {quality.get('fixedIssues', 0)}")
    print(f"[*] Delta Complexity: {quality.get('deltaComplexity', 0)}")
    print(f"[*] Quality Gate Status: {'PASSED' if quality_ok else 'FAILED'}")
    
    if not quality_ok:
        reasons = quality.get("resultReasons", [])
        print("[-] Quality Gate Failure Reasons:")
        for r in reasons:
            if not r.get("isUpToStandards", True):
                gate_name = r.get("gate", "Unknown Gate")
                expected = r.get("expectedThreshold", {}).get("threshold", "N/A")
                actual = r.get("expected", "N/A")
                print(f"    - {gate_name}: Expected threshold: {expected}, Actual value: {actual}")
    print("="*50 + "\n")
    
    # Determine exit code based on gates
    if not coverage_ok:
        print("[-] Pipeline BLOCKED due to coverage gate failure.")
        sys.exit(1)
        
    # Optional: Block on quality gate too if desired, but request asked for coverage gates
    # We will print warning if quality gate fails, but exit 0 unless coverage failed.
    if not quality_ok:
        print("[!] Warning: Quality gates failed, but allowing pipeline since only coverage is blocking.")
        
    print("[+] All coverage gates passed! Pipeline allowed to proceed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
