from vulnerable_app import insecure_login, execute_user_command, unused_and_unsafe_helper

def test_insecure_login_success():
    # Test valid credentials path
    user = insecure_login("admin", "admin")
    assert user is not None
    assert user[0] == "admin"

def test_insecure_login_failure():
    # Test invalid credentials path
    user = insecure_login("admin", "wrongpassword")
    assert user is None

def test_execute_user_command():
    # Test user command execution path to increase coverage
    output = execute_user_command("world")
    assert "world" in output

def test_unused_and_unsafe_helper():
    # Test unsafe helper function to increase coverage
    result = unused_and_unsafe_helper()
    assert result == [1, 2, 3]
