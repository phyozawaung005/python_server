import random

class CyberHygieneEducator:
    def __init__(self):
        self.quizzes = [
            {
                "question": "What is the best way to create a strong password?",
                "options": [
                    "1. Use your birthdate",
                    "2. Use a mix of letters, numbers, and special characters",
                    "3. Use the word 'password'",
                    "4. Use your pet's name"
                ],
                "answer": 2,
                "feedback": "A strong password should be a mix of letters, numbers, and special characters to make it harder to guess."
            },
            {
                "question": "Which of these is a safe browsing practice?",
                "options": [
                    "1. Clicking on any link in an email",
                    "2. Verifying the URL before entering credentials",
                    "3. Downloading files from unknown sources",
                    "4. Using public Wi-Fi without a VPN"
                ],
                "answer": 2,
                "feedback": "Always verify the URL to ensure it is authentic before entering your credentials."
            },
            {
                "question": "What should you do if you receive an unexpected email attachment?",
                "options": [
                    "1. Open it immediately",
                    "2. Ignore it",
                    "3. Verify the sender before opening",
                    "4. Forward it to a friend"
                ],
                "answer": 3,
                "feedback": "Verify the sender of an email attachment before opening it to avoid malware."
            }
        ]
        self.tips = [
            "Avoid using the same password for multiple accounts.",
            "Enable two-factor authentication whenever possible.",
            "Regularly update your software and antivirus programs.",
            "Be cautious of phishing emails and websites."
        ]

    def start_quiz(self):
        print("Welcome to the Cyber Hygiene Educator Quiz!")
        question = random.choice(self.quizzes)
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if user_answer == question["answer"]:
                print("Correct! " + question["feedback"])
            else:
                print("Incorrect. " + question["feedback"])
        except ValueError:
            print("Invalid input. Please enter a number.")

    def show_tip(self):
        print("\nCyber Hygiene Tip: " + random.choice(self.tips))

    def send_reminder(self, schedule="daily"):
        if schedule == "daily":
            print("Daily Reminder: Stay safe online by practicing good cyber hygiene!")
        elif schedule == "weekly":
            print("Weekly Reminder: Review your cyber hygiene practices and stay protected!")

if __name__ == "__main__":
    educator = CyberHygieneEducator()
    while True:
        print("\nChoose an option:")
        print("1. Take a Cyber Hygiene Quiz")
        print("2. Get a Cyber Hygiene Tip")
        print("3. Receive a Reminder")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            educator.start_quiz()
        elif choice == "2":
            educator.show_tip()
        elif choice == "3":
            schedule = input("Do you want a 'daily' or 'weekly' reminder? ").strip().lower()
            educator.send_reminder(schedule)
        elif choice == "4":
            print("Thank you for using Cyber Hygiene Educator! Stay safe online.")
            break
        else:
            print("Invalid choice. Please try again.")
