# Task 1: User Login Check
# Real-World Application: Authentication systems

def check_login(username, password):
    """
    Check if login credentials are valid
    
    Args:
        username: User's username
        password: User's password
    
    Returns:
        None (prints result)
    """
    # Correct credentials
    correct_username = "admin"
    correct_password = "1234"
    
    # Check if both match
    if username == correct_username and password == correct_password:
        print("Login Successful")
    else:
        print("Invalid Credentials")

# Test the function
username = "admin"
password = "1234"
check_login(username, password)

# Test with wrong credentials
print("\nTesting with wrong credentials:")
check_login("admin", "wrong")
check_login("user", "1234")
