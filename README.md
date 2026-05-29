# Codacy Features Demonstration Repository

Manage code quality, track code coverage, and capture static analysis security testing (SAST) issues using Codacy.

## Codacy Status Badges
| Code Quality (Grade) | Code Coverage |
| :---: | :---: |
| [![Codacy Badge](https://app.codacy.com/project/badge/Grade/7ab009634b8f4ebf9df06578198a2d5a)](https://app.codacy.com?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) | [![Codacy Badge](https://app.codacy.com/project/badge/Coverage/7ab009634b8f4ebf9df06578198a2d5a)](https://app.codacy.com?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage) |

---

## Purpose
This repository is designed to showcase the power of Codacy's automated review system. It contains intentionally structured "bad" Python code featuring typical security vulnerabilities (SAST) and code smells, coupled with a pytest suite offering partial test coverage to demonstrate both of Codacy's core modules.

## Deliberate SAST & Quality Issues Included

The file [vulnerable_app.py](file:///Users/andreadasilva/Documents/Repository/Codacy-Repo/vulnerable_app.py) showcases the following anti-patterns:
1.  **SQL Injection (SQLi)**: Dynamically formatted raw SQLite query construction susceptible to injection.
2.  **Hardcoded Credentials**: Storing a plain-text secret API key (`sk-live-5678-...`) directly in the source code.
3.  **Weak Cryptographic Hash**: Hashing passwords using the deprecated `MD5` algorithm.
4.  **Command Injection**: Executing shell commands directly using `subprocess.Popen(..., shell=True)` with raw user input.
5.  **Unsafe Expression Evaluation**: Evaluating unvalidated input dynamically via the `eval()` helper.
6.  **Code Smells**: Variable name shadowing (`list`), dead code blocks, and unused import warnings (`sys`).

---

## Test & Coverage Setup

The repository utilizes [pytest](https://docs.pytest.org/) and [pytest-cov](https://pytest-cov.readthedocs.io/) to measure code coverage:
*   [test_vulnerable_app.py](file:///Users/andreadasilva/Documents/Repository/Codacy-Repo/test_vulnerable_app.py) tests only the safe code paths in the authentication function.
*   The dangerous command execution and dead code helpers are left completely uncovered to show coverage deficit tracking on your Codacy dashboard.

To run the tests and generate a coverage report locally:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest --cov=. --cov-report=xml
```

---

## GitHub Actions CI/CD Integration

The workflow in [.github/workflows/codacy.yml](file:///Users/andreadasilva/Documents/Repository/Codacy-Repo/.github/workflows/codacy.yml) is fully automated to run on every commit or pull request. It consists of two primary jobs:

### 1. Test and Coverage
*   Sets up Python and installs dependencies.
*   Runs unit tests to generate the `coverage.xml` report.
*   Uses `codacy/codacy-coverage-reporter-action@v1` to securely upload coverage metrics using the account-level `CODACY_API_TOKEN` secret.

### 2. SAST Analysis
*   Downloads the official `codacy-analysis-cli` tool.
*   Executes full static analysis locally in the runner environment.
*   Uploads findings to your Codacy dashboard for tracking.
