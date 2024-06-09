import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """
    Generate a random password based on the specified criteria.

    :param length: Length of the password
    :param use_letters: Include letters in the password
    :param use_numbers: Include numbers in the password
    :param use_symbols: Include symbols in the password
    :return: Generated password
    """
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No character types selected. Please select at least one character type.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """
    Main function to run the password generator.
    """
    print("Welcome to the Password Generator")

    try:
        # Prompt the user for password criteria
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        # Generate the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)

        # Display the generated password
        print(f"\nGenerated Password: {password}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
