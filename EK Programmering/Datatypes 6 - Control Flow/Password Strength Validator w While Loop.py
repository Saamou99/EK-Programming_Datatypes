#Password Strength Validator with While Loop
#Create a password validation system that keeps asking for input until a strong password is provided:

#1. Use a while loop to repeatedly ask for password input.

#2. Password must meet ALL criteria:
#• At least 12 characters long
#• Contains at least one number
#• For each failed attempt, tell the user what's missing

#3. When a valid password is entered, display "Strong password accepted!"

#4. Count and display total attempts made

#---

# Initialize attempt counter
attempts = 0

# Start infinite loop (runs until we break it)
while True:

    # Ask user for password
    password = input("Enter a password: ")

    # Increase attempt counter
    attempts += 1

    # Check if password is at least 12 characters long
    is_long_enough = len(password) >= 12

    # Check if password contains at least one number
    has_number = False
    for char in password:
        if char.isdigit():  # Check if character is a digit
            has_number = True
            break           # Stop checking once a number is found

    # If password meets ALL requirements
    if is_long_enough and has_number:
        print("Strong password accepted!")
        print("Total attempts:", attempts)
        break  # Exit loop when password is valid

    else:
        # Tell user what is missing
        print("Password is not strong enough.")

        if not is_long_enough:
            print("- Must be at least 12 characters long.")

        if not has_number:
            print("- Must contain at least one number.")

        print()  # Blank line for readability

#---

#Bonus Challenge:

#1.  Add a maximum attempt limit (5 tries)

#2. If max attempts reached, display "Account creation failed"

# Initialize attempt counter
attempts = 0

# Set maximum allowed attempts
max_attempts = 5

# Start while loop (runs until attempts reach max_attempts)
while attempts < max_attempts:

    # Ask user for password
    password = input("Enter a password: ")

    # Increase attempt counter
    attempts += 1

    # Check if password is at least 12 characters long
    is_long_enough = len(password) >= 12

    # Check if password contains at least one number
    has_number = False
    for char in password:
        if char.isdigit():   # Check if character is a digit
            has_number = True
            break            # Stop checking once a number is found

    # If password meets ALL requirements
    if is_long_enough and has_number:
        print("Strong password accepted!")
        print("Total attempts:", attempts)
        break  # Exit loop if password is valid

    else:
        # Tell user what is missing
        print("Password is not strong enough.")

        if not is_long_enough:
            print("- Must be at least 12 characters long.")

        if not has_number:
            print("- Must contain at least one number.")

        print("Attempts remaining:", max_attempts - attempts)
        print()

# This runs only if max attempts were reached without break
if attempts == max_attempts and not (is_long_enough and has_number):
    print("Account creation failed")
    print("Total attempts:", attempts)
