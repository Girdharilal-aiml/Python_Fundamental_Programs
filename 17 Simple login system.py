def simple_login():
    correct_username = "admin"
    correct_password = "pass123"
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login Successful!")
    else:
        print("Invalid credentials!")
