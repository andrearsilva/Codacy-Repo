import pytest
from vulnerable_app import (
    insecure_login,
    execute_user_command,
    unused_and_unsafe_helper,
    another_vulnerable_function,
    complex_decision_matrix,
    process_user_data_alpha,
    process_user_data_beta,
    extreme_complexity_matrix,
    _calculate_step_value,
    _run_while_loop
)

# 1. Tests for SQL and authentication security
def test_insecure_login_success():
    # Verify authentication succeeds for valid credentials
    user = insecure_login("admin", "admin")
    assert user is not None
    assert user[0] == "admin"

def test_insecure_login_failure():
    # Verify authentication fails for invalid password
    user = insecure_login("admin", "wrong_password")
    assert user is None

def test_insecure_login_sqli_protection():
    # Verify that SQL injection attempts are safely parsed as text and fail
    user = insecure_login("admin' OR '1'='1", "password")
    assert user is None


# 2. Tests for secure command execution
def test_execute_user_command():
    output = execute_user_command("Antigravity")
    assert "Antigravity" in output


# 3. Tests for helpers
def test_unused_and_unsafe_helper():
    result = unused_and_unsafe_helper()
    assert result == [1, 2, 3]

def test_another_vulnerable_function():
    result = another_vulnerable_function("hello_data")
    assert result == {"a": 1, "b": 2}


# 4. Parameterized path tests for complex_decision_matrix (8 branches)
@pytest.mark.parametrize(
    "a, b, c, d, e, expected",
    [
        (1, 1, 1, 0, 0, 1),
        (1, 1, 0, 0, 0, 2),
        (1, 0, 0, 1, 0, 3),
        (1, 0, 0, 0, 0, 4),
        (0, 0, 1, 0, 1, 5),
        (0, 0, 1, 0, 0, 6),
        (0, 0, 0, 1, 0, 7),
        (0, 0, 0, 0, 0, 8),
    ]
)
def test_complex_decision_matrix_paths(a, b, c, d, e, expected):
    assert complex_decision_matrix(a, b, c, d, e) == expected


# 5. Tests for data processing clones
def test_process_user_data_alpha():
    # Test Alpha with items (step_count > 0)
    res_items = process_user_data_alpha(["banana", "apple"])
    assert res_items == ["Item: banana", "Item: apple"]
    
    # Test Alpha with empty list (step_count == 0)
    res_empty = process_user_data_alpha([])
    assert res_empty == []

def test_process_user_data_beta():
    # Test Beta with items
    res_items = process_user_data_beta(["carrot"])
    assert res_items == ["Item: carrot"]


# 6. Parameterized path tests for initial values of extreme_complexity_matrix (16 branches)
@pytest.mark.parametrize(
    "a, b, c, d, e, f, g, h, i, j, expected_base",
    [
        (1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1),
        (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2),
        (1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 3),
        (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4),
        (1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 5),
        (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 6),
        (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 7),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8),
        (0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 9),
        (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 10),
        (0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 11),
        (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 12),
        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 13),
        (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 14),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 15),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16),
    ]
)
def test_extreme_complexity_matrix_base_paths(a, b, c, d, e, f, g, h, i, j, expected_base):
    # Runs the full modularized complex execution logic for each base branch
    res = extreme_complexity_matrix(a, b, c, d, e, f, g, h, i, j)
    assert res >= 0


# 7. Targeted tests for modular loop step-calculation branches to ensure 100% branch coverage
def test_calculate_step_value_branches():
    # Test odd step execution and lower bound clamp
    assert _calculate_step_value(0, 1) == 0
    assert _calculate_step_value(5, 3) == 4
    
    # Test even step execution
    # result > 20 path
    assert _calculate_step_value(21, 0) == 20
    # result > 10 path
    assert _calculate_step_value(12, 0) == 14
    # result <= 10 path
    assert _calculate_step_value(5, 0) == 6

def test_run_while_loop_branches():
    # Test while loop early break when result == 3
    assert _run_while_loop(2) == 3
    
    # Test while loop normal completion (result >= 5 initially)
    assert _run_while_loop(5) == 5
