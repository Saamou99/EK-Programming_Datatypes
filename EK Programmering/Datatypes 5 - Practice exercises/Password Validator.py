# Create a program that checks if a password meets basic security requirements:

#Your password to check
#password = "MyP@ssw0rd"

#Your program should:
# 1. Check if the password is at least 8 characters long

# 2. Check if it contains the character "@" or "!"

# 3. Print the length of the password

# 4. Convert the password to uppercase and print it

# 5. Print True or False if the password meets both requirements (length AND special char)

thisPassword = "MyP@ssw0rd"

# 1. Check length
checkLenght = len(thisPassword) >= 8

# 2. Check for special character
checkSpecialCharacther = "@" in thisPassword or "!" in thisPassword

# 3. Print length
print("Password length:", len(thisPassword))

# 4. Convert to uppercase
print("Uppercase password:", thisPassword.upper())

# 5. Check both requirements
isValid = checkLenght and checkSpecialCharacther
print("Meets security requirements:", isValid)