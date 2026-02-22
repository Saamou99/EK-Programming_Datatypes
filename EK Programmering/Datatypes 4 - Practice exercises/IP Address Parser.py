#You received an IP address as a string and need to extract information from it.
#ip_address = "192.168.1.100"

# Your program should:

# 1. Split the IP address into its four octets (parts) and store in a list

# 2. Print the list of octets

# 3. Print the first octet

# 4. Print the last octet

# 5. Join the octets back together with dashes (-) instead of dots

# Result should be: "192-168-1-100"

ip_address = "192.168.1.100"

# 1. Split into octets
octets = ip_address.split(".")

# 2. Print list
print(octets)

# 3. First octet
print("First:", octets[0])

# 4. Last octet
print("Last:", octets[-1])

# 5. Join with dashes
new_ip = "-".join(octets)
print(new_ip)
