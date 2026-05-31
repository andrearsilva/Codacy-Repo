# Code Quality & Complexity Issues Demo File
# This file is intentionally designed to trigger static analysis, linting, complexity, and duplication warnings.

import os
import sys
import math
import datetime

def process_user_input_data(data):
    # 1. Unused local variable (Lint/Quality warning)
    temporary_secret_key = "secret_12345"
    
    # 2. Duplicate dictionary keys (Lint warning)
    duplicate_dict = {"a": 1, "a": 2}
    
    print("Processing user input data completed.")
    return duplicate_dict

def complex_matrix_decision(a, b, c, d, e):
    # 3. High Cyclomatic Complexity (Complexity warning)
    # Extremely nested conditional branches to inflate complexity metrics
    score = 0
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    score = 1
                else:
                    score = 2
            else:
                if e > 0:
                    score = 3
                else:
                    score = 4
        else:
            if c > 0:
                if d > 0:
                    score = 5
                else:
                    score = 6
            else:
                score = 7
    else:
        if b > 0:
            if c > 0:
                if d > 0:
                    score = 8
                else:
                    score = 9
            else:
                score = 10
        else:
            score = 11
            
    return score

def compute_alpha_score_sequence(numbers):
    # 4. Code Duplication Clone Alpha (Duplication warning)
    print("Initiating score calculation sequence alpha...")
    total_accumulated_score = 0
    step_multiplier = 2
    
    for num in numbers:
        adjusted_value = num * step_multiplier
        total_accumulated_score += adjusted_value
        print(f"Step adjustment log: value {num} multiplied to {adjusted_value}. Total: {total_accumulated_score}")
        
    print("Score calculation sequence alpha completed successfully.")
    return total_accumulated_score

def compute_beta_score_sequence(numbers):
    # 5. Code Duplication Clone Beta (Duplication warning - identical clone of Alpha)
    print("Initiating score calculation sequence alpha...")
    total_accumulated_score = 0
    step_multiplier = 2
    
    for num in numbers:
        adjusted_value = num * step_multiplier
        total_accumulated_score += adjusted_value
        print(f"Step adjustment log: value {num} multiplied to {adjusted_value}. Total: {total_accumulated_score}")
        
    print("Score calculation sequence alpha completed successfully.")
    return total_accumulated_score

def execute_dynamic_logic(formula):
    # 6. Unsafe eval call (SAST warning)
    eval(formula)

def demo_style_and_character_limit_violations():
    # 7. PEP8 / Style issues (Line exceeding 79 characters, double trailing whitespaces)
    print("This printed line is extremely long and intentionally exceeds the standard PEP8 maximum character limit of 79 characters to trigger a style warning"  ) 
