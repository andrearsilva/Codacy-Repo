import os
import sqlite3
import hashlib
import sys # Unused import (will trigger code quality warnings)

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
