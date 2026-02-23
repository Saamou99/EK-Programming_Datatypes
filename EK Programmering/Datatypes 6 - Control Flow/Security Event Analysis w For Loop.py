# Security Event Analysis with For Loop
# Create a security monitoring system that analyzes a list of events:

# 1. Create a list of security events (strings) that includes:
# a. Normal events: 'user login', 'file access', 'email sent' 
# b. Suspicious events: 'failed login', 'unauthorized access', 'malware detected'

# 2. Use a for loop to process each event and:
# a. Count total events processed
# b. Count suspicious events (events containing 'failed', 'unauthorized', or 'malware')
# c. Print each suspicious event with 'ALERT:' prefix
# d. Print normal events with 'OK:' prefix

# 3. After the loop, display:
# a. Total events processed
# b. Number of suspicious events found
# c. Security status: 'SECURE' if no suspicious events, 'AT RISK' if any found


# Create list of security events
security_events = [
    "user login",
    "file access",
    "email sent",
    "failed login",
    "unauthorized access",
    "malware detected"
]

# Initialize counters
total_events = 0
suspicious_count = 0

# Loop through each event
for event in security_events:

    # Increase total event counter
    total_events += 1

    # Check if event is suspicious
    if "failed" in event or "unauthorized" in event or "malware" in event:
        suspicious_count += 1
        print("ALERT:", event)
    else:
        print("OK:", event)

# After loop - print summary
print("\n--- SUMMARY ---")
print("Total events processed:", total_events)
print("Suspicious events found:", suspicious_count)

# Determine security status
if suspicious_count > 0:
    print("Security status: AT RISK")
else:
    print("Security status: SECURE")

#---

#Bonus Challenge:

# 1. Use break to stop processing if 'critical threat' is found
# 2. Use continue to skip events containing 'test'
# 3. Add event numbering in the output(Hint: enumerate())

# Create list of security events (including bonus cases)
security_events = [
    "user login",
    "file access",
    "test event",
    "failed login",
    "email sent",
    "unauthorized access",
    "malware detected",
    "critical threat"
]

# Initialize counters
total_events = 0
suspicious_count = 0

# Loop with numbering (starting at 1)
for index, event in enumerate(security_events, start=1):

    # Skip test events
    if "test" in event:
        continue  # Skip this event and move to next

    # Increase total event counter
    total_events += 1

    # Stop immediately if critical threat is found
    if "critical threat" in event:
        print(f"{index}. ALERT: {event.upper()} !!!")
        print("CRITICAL threat detected. Stopping analysis.")
        break

    # Check if event is suspicious
    if "failed" in event or "unauthorized" in event or "malware" in event:
        suspicious_count += 1
        print(f"{index}. ALERT: {event}")
    else:
        print(f"{index}. OK: {event}")

# Print summary
print("\n--- SUMMARY ---")
print("Total events processed:", total_events)
print("Suspicious events found:", suspicious_count)

# Determine security status
if suspicious_count > 0:
    print("Security status: AT RISK")
else:
    print("Security status: SECURE")