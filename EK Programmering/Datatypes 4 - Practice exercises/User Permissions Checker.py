#Create a user access control system using a dictionary:
# Create a dictionary with user information

#user = {

#"username": "alice_admin",

#"role": "administrator",

#"access_level": 5,

#"account_active": True

#}

# Your program should:

# 1. Print the username

# 2. Print the user's role

# 3. Check if access_level is greater than 3 AND account_active is True

# 4. Add a new key "last_login" with value "2026-02-13"

# 5. Update the access_level to 4

# 6. Print all the keys in the dictionary

# 7. Print all the values in the dictionary

user = {
    "username": "alice_admin",
    "role": "administrator",
    "access_level": 5,
    "account_active": True
}

# 1
print(user["username"])

# 2
print(user["role"])

# 3
has_access = user["access_level"] > 3 and user["account_active"]
print("Access allowed:", has_access)

# 4
user["last_login"] = "2026-02-13"

# 5
user["access_level"] = 4

# 6
print("Keys:", user.keys())

# 7
print("Values:", user.values())