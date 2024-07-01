# Password Complexity Checker

"""
  This program checks the strength of a password based on the following criteria:
  - Minimum length of 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character

"""

import re

# password_strength returns the password strength 
def password_strength(password):

    strength = -1

    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        strength += 1
    return strength

# Recommends the User to strengthen the password
def tips(password):
    print("Tips:-")

    if len(password) < 8:
        print("- Minimum length of 8 characters")
    if not (re.search(r'[A-Z]', password)):
        print("- At least one uppercase letter")
    if not (re.search(r'[a-z]', password)):
        print("- At least one lowercase letter")
    if not (re.search(r'\d', password)):
        print("- At least one digit")
    if not (re.search(r'[!@#$%^&*(),.?\":{}|<>]', password)):
        print("- At least one special character")

# main() function
while True:
    # Asks user for password input.
    password = input("Enter your password: ")
    # password_strength() returns the strength of the password.
    strength = password_strength(password)

    # strength_type[] shows the different strength.
    strength_type = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    print("Your password is" , strength_type[strength] , ".")

    # if password is not Very Strong then it calls Tips().
    if strength != 4:
        tips(password)
    
    # To continue or exit
    choice = input("Press any key to continue or (n/N) to stop: ")
    if choice == 'N' or choice == 'n':
        break

