#Store and manipulate port scan results:

# Ports are stored as a tuple (obs!: immutable)
#open_ports = (22, 80, 443, 8080)

# Your program should:

# 1. Print all open ports

# 2. Print the first open port

# 3. Try to check if port 443 is in the tuple

# 4. Add port 3389

# 5. Add port 21

# 6. Print the final tuple

open_ports = (22, 80, 443, 8080)

# 1
print(open_ports)

# 2
print("First port:", open_ports[0])

# 3
print("Is 443 open?", 443 in open_ports)

# 4 & 5 (convert to list first)
ports_list = list(open_ports)
ports_list.append(3389)
ports_list.append(21)

# Convert back to tuple
open_ports = tuple(ports_list)

# 6
print("Final tuple:", open_ports)