from vulnerable_app import insecure_login

def test_insecure_login_success():
    # Test valid credentials path
    user = insecure_login("admin", "admin")
    assert user is not None
    assert user[0] == "admin"

def test_insecure_login_failure():
    # Test invalid credentials path
    user = insecure_login("admin", "wrongpassword")
    assert user is None
