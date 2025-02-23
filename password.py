import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    
    for i in range(length):
        password += random.choice(characters)
    return password

length = input("Enter the password length: ")

# Check if the input is a valid number
if length.isdigit():
    length = int(length)
    print("Generated Password:", generate_password(length))
else:
    print("Please enter a valid number.")
