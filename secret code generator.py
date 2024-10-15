def encode(message, shift):
    # Initialize an empty string for the encoded message
    encoded_message = ""
    # Loop through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Calculate the effective shift within the alphabet range
            shift_amount = shift % 26
            # Convert the character to lowercase, shift it, and convert it back to a character
            new_char = chr((ord(char.lower()) - 97 + shift_amount) % 26 + 97)
            # If the original character was uppercase, convert the new character to uppercase
            if char.isupper():
                new_char = new_char.upper()
            # Append the new character to the encoded message
            encoded_message += new_char
        else:
            # If the character is not a letter, leave it unchanged
            encoded_message += char
    # Return the complete encoded message
    return encoded_message

def decode(message, shift):
    # Decode the message by encoding it with a negative shift
    return encode(message, -shift)

def secret_code_generator():
    while True:
        # Display the menu options
        print("\nSecret Code Generator Menu:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")

        # Prompt the user for their choice
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            # If the user chooses to encode a message
            message = input("Enter the message to encode: ")
            shift = int(input("Enter the shift amount: "))
            # Print the encoded message
            print("Encoded Message:", encode(message, shift))
        elif choice == '2':
            # If the user chooses to decode a message
            message = input("Enter the message to decode: ")
            shift = int(input("Enter the shift amount: "))
            # Print the decoded message
            print("Decoded Message:", decode(message, shift))
        elif choice == '3':
            # If the user chooses to exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            # If the user enters an invalid choice
            print("Error: Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    # Call the secret_code_generator function to start the program
    secret_code_generator()
