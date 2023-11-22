import random
import string

class PasswordGenerator:
    def generate_password(self, length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special_chars=True):
        characters = ""
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_numbers:
            characters += string.digits
        if use_special_chars:
            characters += string.punctuation

        if not characters:
            print("Error: Please select at least one character type.")
            return None

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def main():
    password_generator = PasswordGenerator()

    print("Welcome to the Password Generator!")

    while True:
        length = int(input("Enter the desired length of the password: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

        generated_password = password_generator.generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_numbers=use_numbers,
            use_special_chars=use_special_chars
        )

        if generated_password:
            print(f"Generated Password: {generated_password}")

        generate_another = input("Generate another password? (yes/no): ")
        if generate_another.lower() != 'yes':
            print("Exiting the Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()

