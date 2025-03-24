while True:
    username = input("Enter Username: ")
    if username == "admin":
        password = input("Enter password: ")
        if password == "asd123":
            print("Login success")
            break  # Exit the loop if login is successful
        else:
            print("Password wrong")
    else:
        print("Username wrong")