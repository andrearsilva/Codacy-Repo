from vulnerable_app import insecure_login, execute_user_command

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
    # Test user command execution path to increase coverage to ~85%
    output = execute_user_command("world")
    assert "world" in output
