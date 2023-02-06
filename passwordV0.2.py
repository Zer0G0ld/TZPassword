#!/usr/bin/env python

import random
import string

print("==============================================")
print("")
print("                Password Generator            ")
print("")
print("==============================================")
print("")

def generate_password(purpose, security_level):
    # Defines the set of characters that will be used in the password
    chars = string.ascii_letters + string.digits + string.punctuation

    # Sets the minimum password length based on the desired security level
    if security_level == "low":
        min_length = 12
    elif security_level == "medium":
        min_length = 16
    else:
        min_length = 20

    # Adds information about the purpose of the password to the beginning of the password
    password = purpose + ":"

    # Generates a random password with the specified minimum length
    while len(password) < min_length:
        password += random.choice(chars)

    return password

# Receive user input
purpose = input("For what purpose do you need a password? ")
security_level = input("What is the desired security level (low, medium or high)? ")

# Generate and display the password
password = generate_password(purpose, security_level)
print("Your new password is: ", password)

