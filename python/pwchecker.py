def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Weak: Include at least one number."
    if not any(char.isupper() for char in password):
        return "Moderate: Add some uppercase letters for more security."
    if not any(char.islower() for char in password):
        return "Moderate: Add some lowercase letters for more security."
    if not any(char in "!@#$%^&*()_+" for char in password):
        return "Strong: But consider adding special characters for the best security."
    return "Very Strong: This is a secure password!"
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
