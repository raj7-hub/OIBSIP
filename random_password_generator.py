import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    """Generate a random password based on user preferences."""
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters  
    if use_digits:
        characters += string.digits         
    if use_symbols:
        characters += string.punctuation   

    if not characters:
        return " No character set selected. Please enable at least one option."

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Ask user for password length
        length = int(input("Enter password length: "))
        if length <= 0:
            print(" Password length must be greater than 0.")
            return

        # Ask for character preferences
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate and show password
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"\n Generated Password: {password}")

    except ValueError:
        print(" Invalid input! Please enter numeric values for length.")

if __name__ == "__main__":
    main()
