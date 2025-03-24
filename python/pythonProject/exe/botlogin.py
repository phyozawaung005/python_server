import random

from pythonProject.login import password

# Define responses
responses = {
    "calculate": ['Input Something'],  # You can add more responses here
    "hi": ["Hi there"],
    "default": ["I'm sorry, I don't understand."],

}

# Define user credentials
users = {
    "Phyo Zaw Aung": "Linn Myat Mon",
    "user2": "password2",
}

# Function to authenticate user
def authenticate(username, password):
    return username in users and users[username] == password


# Main loop
while True:
    # Login loop
    while True:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if authenticate(username, password):
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")

    # Chatbot loop
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'quit':
            choice = input("Do you want to exit? (yes/no): ")
            if choice.lower() == "yes":
                print("Process finished.")
                exit()  # Exit the program
            elif choice.lower() == "no":
                continue  # Break out of the chatbot loop to go back to login
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                continue  # Continue the loop to ask again

        response = random.choice(responses.get(user_input, responses["default"]))
        print("Chatbot:", response)

        # Check if the user wants to do calculations
        if user_input == 'calculate':
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            operation = input("Choose +, -, *, /, %: ")

            print('Number 1:', a)
            print('Number 2:', b)

            if operation == '+':
                result = a + b
            elif operation == '-':
                result = a - b
            elif operation == '*':
                result = a * b
            elif operation == '/':
                if b != 0:
                    result = a / b
                else:
                    print("Error: Division by zero!")
                    continue  # Skip further processing
            elif operation == '%':
                result = a % b
            else:
                print("Invalid operation!")
                continue  # Skip further processing

            print('Result:', result)
            if result % 2 == 0:
                print('Result is even.')
            else:
                print('Result is odd.')
