#Maintain a list of blocked IP addresses using sets:

#blocked_ips = {"10.0.0.5", "192.168.1.100", "172.16.0.50"}
#new_threats = {"192.168.1.100", "10.0.0.99", "8.8.8.8"}

# Your program should:

# 1. Print the blocked_ips set

# 2. Add "203.0.113.0" to blocked_ips

# 3. Check if "8.8.8.8" is in blocked_ips (should print False initially)

# 4. Find which IPs are in BOTH blocked_ips and new_threats (hint: intersection)

# 5. Combine blocked_ips and new_threats into one set (hint: union)

# 6. Remove "10.0.0.5" from blocked_ips

# 7. Print the final blocked_ips set

blocked_ips = {"10.0.0.5", "192.168.1.100", "172.16.0.50"}
new_threats = {"192.168.1.100", "10.0.0.99", "8.8.8.8"}

# 1
print(blocked_ips)

# 2
blocked_ips.add("203.0.113.0")

# 3
print("8.8.8.8 in blocked:", "8.8.8.8" in blocked_ips)

# 4
print("Intersection:", blocked_ips.intersection(new_threats))

# 5
print("Union:", blocked_ips.union(new_threats))

# 6
blocked_ips.remove("10.0.0.5")

# 7
print("Final blocked:", blocked_ips)