import os
import sqlite3
import hashlib
import sys # Unused import (will trigger code quality warnings)
import json # Another unused import to trigger quality checks

# 1. Hardcoded sensitive credential (SAST issue)
SUPER_SECRET_API_KEY = "sk-live-5678-abcde-99999-mysecretkey"

def insecure_login(username, password):
    # 2. Insecure MD5 hashing for passwords (SAST issue)
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    # 3. SQL Injection vulnerability (SAST issue)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create a dummy table for demonstration
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', '21232f297a57a5a743894a0e4a801fc3')") # MD5 of 'admin'
    
    # Vulnerable raw query construction
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{hashed_password}'"
    
    # Execute the raw query which is vulnerable to injection
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

def execute_user_command(user_input):
    # 4. Command Injection vulnerability (SAST issue)
    # Using shell=True with raw user input allows executing arbitrary system commands
    import subprocess
    cmd = f"echo {user_input}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

def unused_and_unsafe_helper():
    # 5. Shadowing built-in, dead code, and unsafe eval()
    # Shadowing 'list' built-in name
    list = [1, 2, 3]
    
    # Unsafe eval usage (SAST issue)
    user_payload = "print('Hello')"
    eval(user_payload)
    
    # Unreachable code block
    return list
    unused_variable = "I am never used"

def another_vulnerable_function(data):
    # 6. Unsafe exec() execution (SAST critical issue)
    exec(data)
    
    # 7. Lint issue: duplicate dictionary keys
    bad_dict = {"a": 1, "a": 2}
    
    # 8. Lint issue: unused local variable
    unused_val = bad_dict

def complex_decision_matrix(a, b, c, d, e):
    # 9. High Cyclomatic Complexity (demonstrates Codacy complexity analysis)
    result = 0
    if a > 0:
        if b > 0:
            if c > 0:
                result = 1
            else:
                result = 2
        else:
            if d > 0:
                result = 3
            else:
                result = 4
    else:
        if c > 0:
            if e > 0:
                result = 5
            else:
                result = 6
        else:
            if d > 0:
                result = 7
            else:
                result = 8
    return result

def process_user_data_alpha(data):
    # 10. Code Duplication Issue (demonstrates Codacy duplication engine)
    print("Initializing system data structures...")
    print("Loading external user profiles...")
    print("Starting user data processing sequence Alpha...")
    status = "Pending"
    log_entries = []
    
    # Block 1 of processing
    step_count = 0
    for item in data:
        processed = f"Item: {item}"
        log_entries.append(processed)
        print(f"Logged Alpha Step {step_count}: {processed}")
        step_count += 1
        
    # Block 2 of processing
    verification_status = True
    if step_count > 0:
        print("Verifying database records...")
        verification_status = True
    else:
        print("Warning: No database records processed!")
        verification_status = False
        
    # Block 3 of processing
    print("Updating central cache configuration...")
    cache_updated = True
    if cache_updated:
        print("Central cache synced successfully.")
    else:
        print("Cache sync failed.")
        
    # Finalization block
    status = "Complete"
    print(f"Finished sequence Alpha. Status: {status}")
    print(f"Verification Check: {verification_status}")
    print("Cleaning temporary buffer directories...")
    print("Process sequence completed successfully!")
    return log_entries

def process_user_data_beta(data):
    # Deliberate identical duplicate of the function above to trigger code clone/duplication analysis
    print("Initializing system data structures...")
    print("Loading external user profiles...")
    print("Starting user data processing sequence Alpha...")
    status = "Pending"
    log_entries = []
    
    # Block 1 of processing
    step_count = 0
    for item in data:
        processed = f"Item: {item}"
        log_entries.append(processed)
        print(f"Logged Alpha Step {step_count}: {processed}")
        step_count += 1
        
    # Block 2 of processing
    verification_status = True
    if step_count > 0:
        print("Verifying database records...")
        verification_status = True
    else:
        print("Warning: No database records processed!")
        verification_status = False
        
    # Block 3 of processing
    print("Updating central cache configuration...")
    cache_updated = True
    if cache_updated:
        print("Central cache synced successfully.")
    else:
        print("Cache sync failed.")
        
    # Finalization block
    status = "Complete"
    print(f"Finished sequence Alpha. Status: {status}")
    print(f"Verification Check: {verification_status}")
    print("Cleaning temporary buffer directories...")
    print("Process sequence completed successfully!")
    return log_entries

def extreme_complexity_matrix(a, b, c, d, e, f, g, h, i, j):
    # 11. Extreme High Cyclomatic Complexity to trigger gate policy
    result = 0
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    result = 1
                else:
                    result = 2
            else:
                if e > 0:
                    result = 3
                else:
                    result = 4
        else:
            if f > 0:
                if g > 0:
                    result = 5
                else:
                    result = 6
            else:
                if h > 0:
                    result = 7
                else:
                    result = 8
    else:
        if i > 0:
            if j > 0:
                if c > 0:
                    result = 9
                else:
                    result = 10
            else:
                if d > 0:
                    result = 11
                else:
                    result = 12
        else:
            if e > 0:
                if f > 0:
                    result = 13
                else:
                    result = 14
            else:
                if g > 0:
                    result = 15
                else:
                    result = 16
                    
    # Additional loops and conditions to increase metric over 100
    for x in range(10):
        if x % 2 == 0:
            result += 1
            if result > 20:
                result -= 2
            elif result > 10:
                result += 1
        else:
            result -= 1
            if result < 0:
                result = 0
                
    while result < 5:
        result += 1
        if result == 3:
            break
            
    return result
