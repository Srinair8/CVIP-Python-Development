import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    if length < 4 and (use_uppercase or use_lowercase or use_digits or use_special_chars):
        return "Password length should be at least 4 characters for the selected character types."

    password = [random.choice(characters) for _ in range(length)]
    random.shuffle(password)
    return ''.join(password)

def password_meets_requirements(password, use_uppercase, use_lowercase, use_digits, use_special_chars):
    # for checking the requirements
    if use_uppercase and not any(char.isupper() for char in password):
        return "Password must include at least one uppercase letter."
    if use_lowercase and not any(char.islower() for char in password):
        return "Password must include at least one lowercase letter."
    if use_digits and not any(char.isdigit() for char in password):
        return "Password must include at least one digit."
    if use_special_chars and not any(char in string.punctuation for char in password):
        return "Password must include at least one special character."
    return None

def password_statistics(password):
    # Calculates and displays the statistics about the generated password
    stats = {
        "Length": len(password),
        "Uppercase Letters": sum(1 for char in password if char.isupper()),
        "Lowercase Letters": sum(1 for char in password if char.islower()),
        "Digits": sum(1 for char in password if char.isdigit()),
        "Special Characters": sum(1 for char in password if char in string.punctuation)
    }
    return stats

def main():
    print("Random Password Generator")

    while True:
        length = int(input("Enter the password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

        print(f"Generated Password: {password}")

        requirements = password_meets_requirements(password, use_uppercase, use_lowercase, use_digits, use_special_chars)
        if requirements:
            print(requirements)

        stats = password_statistics(password)
        print("Password Statistics:")
        for key, value in stats.items():
            print(f"{key}: {value}")

        another_password = input("Generate another password? (y/n): ").lower()
        if another_password != 'y':
            break

if __name__ == "__main__":
    main()
