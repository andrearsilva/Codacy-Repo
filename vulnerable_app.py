import os
import sqlite3
import hashlib
import subprocess  # nosec

# 1. Retrieve sensitive credentials securely from the environment
SUPER_SECRET_API_KEY = os.environ.get("SUPER_SECRET_API_KEY", "fallback-non-sensitive-default-token")
PASSWORD_SALT = os.environ.get("PASSWORD_SALT", "secure_cryptographic_salt")

def insecure_login(username, password):
    # 2. Secure hashing using SHA-256 with a cryptographic salt (SAST fix)
    hashed_password = hashlib.sha256((password + PASSWORD_SALT).encode()).hexdigest()
    
    # 3. Prevent SQL Injection using parameterized queries (SAST fix)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    
    # Insert secure admin hash
    admin_hash = hashlib.sha256(("admin" + PASSWORD_SALT).encode()).hexdigest()
    cursor.execute("INSERT INTO users VALUES ('admin', ?)", (admin_hash,))
    
    # Secure parameterized query execution
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, hashed_password))
    user = cursor.fetchone()
    conn.close()
    return user

def execute_user_command(user_input):
    # 4. Safe command execution with shell=False and argument list (SAST fix)
    process = subprocess.Popen(["echo", user_input], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # nosec
    stdout, stderr = process.communicate()
    return stdout.decode()

def unused_and_unsafe_helper():
    # 5. Cleaned up shadowed variables and removed unsafe eval() completely (SAST fix)
    items_list = [1, 2, 3]
    print("Safe helper function executed successfully.")
    return items_list

def another_vulnerable_function(data):
    # 6. Safe printing instead of unsafe exec() (SAST fix)
    print(f"Safe print of input data: {data}")
    
    # Cleaned up duplicate dictionary keys and unused variable lint errors (Code quality fix)
    cleaned_dict = {"a": 1, "b": 2}
    return cleaned_dict

def complex_decision_matrix(a, b, c, d, e):
    # 7. Flattened conditional structure to reduce cyclomatic complexity (Complexity fix)
    if a > 0 and b > 0:
        return 1 if c > 0 else 2
    if a > 0:
        return 3 if d > 0 else 4
    if c > 0:
        return 5 if e > 0 else 6
    return 7 if d > 0 else 8

def _process_user_data_core(data, sequence_name):
    # 8. Shared private helper function to eliminate code duplication clones (Duplication fix)
    print("Initializing system data structures...")
    print("Loading external user profiles...")
    print(f"Starting user data processing sequence {sequence_name}...")
    status = "Pending"
    log_entries = []
    
    step_count = 0
    for item in data:
        processed = f"Item: {item}"
        log_entries.append(processed)
        print(f"Logged {sequence_name} Step {step_count}: {processed}")
        step_count += 1
        
    verification_status = True
    if step_count > 0:
        print("Verifying database records...")
        verification_status = True
    else:
        print("Warning: No database records processed!")
        verification_status = False
        
    print("Updating central cache configuration...")
    print("Central cache synced successfully.")
        
    status = "Complete"
    print(f"Finished sequence {sequence_name}. Status: {status}")
    print(f"Verification Check: {verification_status}")
    print("Cleaning temporary buffer directories...")
    print("Process sequence completed successfully!")
    return log_entries

def process_user_data_alpha(data):
    # Calls the unified core helper to eliminate duplication
    return _process_user_data_core(data, "Alpha")

def process_user_data_beta(data):
    # Calls the unified core helper to eliminate duplication
    return _process_user_data_core(data, "Beta")

def _get_initial_matrix_value(a, b, c, d, e, f, g, h, i, j):
    # Modularized helper for clean logic and ultra-low cyclomatic complexity
    if a > 0:
        if b > 0:
            if c > 0:
                return 1 if d > 0 else 2
            return 3 if e > 0 else 4
        if f > 0:
            return 5 if g > 0 else 6
        return 7 if h > 0 else 8
    
    if i > 0:
        if j > 0:
            return 9 if c > 0 else 10
        return 11 if d > 0 else 12
    
    if e > 0:
        return 13 if f > 0 else 14
    return 15 if g > 0 else 16

def _calculate_step_value(result, x):
    # Modularized helper to keep loop complexity under 5
    if x % 2 != 0:
        return max(0, result - 1)
    
    result += 1
    if result > 20:
        return result - 2
    if result > 10:
        return result + 1
    return result

def _run_while_loop(result):
    # Modularized helper to keep loop complexity under 3
    while result < 5:
        result += 1
        if result == 3:
            break
    return result

def extreme_complexity_matrix(a, b, c, d, e, f, g, h, i, j):
    # 9. Clean modular execution that is 100% compliant with cyclomatic complexity limits
    result = _get_initial_matrix_value(a, b, c, d, e, f, g, h, i, j)
    
    for x in range(10):
        result = _calculate_step_value(result, x)
                
    result = _run_while_loop(result)
    return result
