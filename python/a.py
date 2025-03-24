def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
  
    username = "Admin"
    password = "asd123"
    if username == username and password == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")
        login()
login()
