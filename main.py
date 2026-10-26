import string
import secrets

def generate_password():
    print("=== Random Password Generator ===")
    
    # 1. Get password length
    while True:
        try:
            length = int(input("Enter password length (minimum 6): "))
            if length < 6:
                print("For security, the password should be at least 6 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # 2. Get user preferences
    use_upper = input("Include uppercase letters? (y/n): ").lower().strip() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower().strip() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower().strip() == 'y'

    # 3. Build the character pool based on answers
    char_pool = string.ascii_lowercase # Always include lowercase letters
    
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # 4. Generate the password securely
    # The secrets module is used instead of random for cryptographic security
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    
    print("\nYour Generated Password:")
    print(password)

if __name__ == "__main__":
    generate_password()