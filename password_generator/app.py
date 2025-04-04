import random
import string

# Function to generate a random password of a given length
def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters and join them to form a password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function to get user input and generate multiple passwords
def main():
    # Ask user how many passwords they want
    num_passwords = int(input("How many passwords would you like to generate? "))
    
    # Ask user for the length of each password
    password_length = int(input("Enter the length of each password: "))
    
    print("\nGenerated Passwords:")
    
    # Generate and display the requested number of passwords
    for _ in range(num_passwords):
        password = generate_password(password_length)
        print(password)

# Call the main function to run the program
if __name__ == "__main__":
    main()
