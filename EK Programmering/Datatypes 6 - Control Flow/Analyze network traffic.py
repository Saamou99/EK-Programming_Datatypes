#Network Protocol Classification with Match-Case
#Create a Python script that analyzes network traffic:

#Requirements
#Get user input for a port number (integer)
#Use match-case to classify the port:

#1. 22 → "SSH - Secure Shell (Critical Security Service)"

#2. 80 → "HTTP - Web Traffic (Unencrypted)"

#3. 443 → "HTTPS - Secure Web Traffic"

#4. 20 or 21 → "FTP - File Transfer (Legacy Protocol)"

#5. 53 → "DNS - Domain Name Resolution"

#6. 25 → "SMTP - Email Transfer"

#7. _ (default) → "Unknown or Custom Port - Investigate"

#Print the protocol name and security note.


#1 Get port number from user
port = int(input("Enter a port number: "))

# Use match-case to classify the port
match port:

    # SSH
    case 22:
        print("SSH - Secure Shell (Critical Security Service)")

    # HTTP
    case 80:
        print("HTTP - Web Traffic (Unencrypted)")

    # HTTPS
    case 443:
        print("HTTPS - Secure Web Traffic")

    # FTP (two possible ports)
    case 20 | 21:
        print("FTP - File Transfer (Legacy Protocol)")

    # DNS
    case 53:
        print("DNS - Domain Name Resolution")

    # SMTP
    case 25:
        print("SMTP - Email Transfer")

    # Default case (anything else)
    case _:
        print("Unknown or Custom Port - Investigate")

#--- 

#Bonus - Extend the script to handle port ranges:

#1. Ports 1-1023: "Well-known system ports"
#2. Ports 1024-49151: "Registered user ports"
#3. Ports 49152-65535: "Dynamic/private ports"

# Import sys to allow exit if needed (optional)
import sys

# Get port number from user
port = int(input("Enter a port number: "))

# First: classify specific well-known ports
match port:

    case 22:
        print("SSH - Secure Shell (Critical Security Service)")

    case 80:
        print("HTTP - Web Traffic (Unencrypted)")

    case 443:
        print("HTTPS - Secure Web Traffic")

    case 20 | 21:
        print("FTP - File Transfer (Legacy Protocol)")

    case 53:
        print("DNS - Domain Name Resolution")

    case 25:
        print("SMTP - Email Transfer")

    case _:
        print("Unknown or Custom Port - Investigate")

# Second: classify port range
# Check that port is valid (1–65535)
if port >= 1 and port <= 1023:
    print("Port Category: Well-known system ports")

elif port >= 1024 and port <= 49151:
    print("Port Category: Registered user ports")

elif port >= 49152 and port <= 65535:
    print("Port Category: Dynamic/private ports")

else:
    print("Invalid port number (must be 1–65535)")