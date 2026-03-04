def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful!"
    else:
        return "Invalid credentials"

def logout():
    return "You have been logged out."
