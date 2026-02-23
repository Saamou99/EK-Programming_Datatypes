#A security monitoring system has logged several events. Analyze the log:

#security_events = ["login_success", "login_failed", "file_access", "login_failed", #"login_success", "login_failed", "malware_detected", "login_failed"]

# Your program should:

# 1. Print how many total events were logged

# 2. Count how many times "login_failed" appears

# 3. Find the index of "malware_detected"

# 4. Add a new event "system_reboot" to the end of the list

# 5. Remove the first "login_success" from the list

# 6. Print the last 3 events in the log

mySecurityEvents = [
    "login_success", "login_failed", "file_access", "login_failed",
    "login_success", "login_failed", "malware_detected", "login_failed"
    ]

# 1
print("Total events:", len(mySecurityEvents))

# 2
print("Login failed count:", mySecurityEvents.count("login_failed"))

# 3
print("Malware index:", mySecurityEvents.index("malware_detected"))

# 4
mySecurityEvents.append("system_reboot")

# 5
mySecurityEvents.remove("login_success")

# 6
print("Last 3 events:", mySecurityEvents[-3:])