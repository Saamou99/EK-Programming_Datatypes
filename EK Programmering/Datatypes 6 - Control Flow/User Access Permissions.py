#Cybersecurity Access Control with If Statements
#Create a Python script that checks user access permissions:

#Get user input for:
#• user_role (admin, analyst, intern, guest)

#• security_clearance (1-5, where 5 is highest)

#Use if-elif-else to determine access level:

#1. user is "admin" → grant "Full Access"

#2. user is "analyst" AND clearance >= 3 → grant "Analyst Access"

#3. user is "intern" AND clearance >= 2 → grant "Limited Access"

#4. user is "guest" → grant "Public Access Only"

#5. Else → deny access

#Print appropriate messages for each condition met.

#Bonus. Add time-based restrictions using the datetime library. Restrict access outside business hours (9-17)

#1 Get user input
user_role = input("Enter user role (admin, analyst, intern, guest): ").lower()
security_clearance = int(input("Enter security clearance (1-5): "))

#2 Access control logic
if user_role == "admin":
    print("Access granted: Full Access")

elif user_role == "analyst" and security_clearance >= 3:
    print("Access granted: Analyst Access")

elif user_role == "intern" and security_clearance >= 2:
    print("Access granted: Limited Access")

elif user_role == "guest":
    print("Access granted: Public Access Only")

else:
    print("Access denied")

#---

#Bonus Time-Based Restriction

from datetime import datetime

# Get current hour
current_hour = datetime.now().hour

# Get user input
user_role = input("Enter user role (admin, analyst, intern, guest): ").lower()
security_clearance = int(input("Enter security clearance (1-5): "))

# Check business hours first
if current_hour < 9 or current_hour >= 17:
    print("Access denied: Outside business hours (9-17)")

else:
    # Access control logic
    if user_role == "admin":
        print("Access granted: Full Access")

    elif user_role == "analyst" and security_clearance >= 3:
        print("Access granted: Analyst Access")

    elif user_role == "intern" and security_clearance >= 2:
        print("Access granted: Limited Access")

    elif user_role == "guest":
        print("Access granted: Public Access Only")

    else:
        print("Access denied")