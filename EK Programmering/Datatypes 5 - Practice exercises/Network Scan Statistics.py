#Calculate statistics from network scan results:
#response_times_ms = [45, 120, 38, 201, 89, 156, 72, 93, 167, 54]

# Your program should:

# 1. Print how many hosts were scanned (length of list)

# 2. Calculate the total response time (sum of all values)

# 3. Calculate the average response time

# 4. Find the fastest response time

# 5. Find the slowest response time

# 6 [BONUS-TASK]. Count how many responses were faster than 100ms (hint: use loop)

# 7 [BONUS-TASK]. Create a new list with all response times divided by 2

response_times_ms = [45, 120, 38, 201, 89, 156, 72, 93, 167, 54]

# 1
print("Hosts scanned:", len(response_times_ms))

# 2
print("Total time:", sum(response_times_ms))

# 3
average = sum(response_times_ms) / len(response_times_ms)
print("Average:", average)

# 4
print("Fastest:", min(response_times_ms))

# 5
print("Slowest:", max(response_times_ms))

# 6 BONUS
faster_than_100 = 0
for time in response_times_ms:
    if time < 100:
        faster_than_100 += 1

print("Faster than 100ms:", faster_than_100)

# 7 BONUS
half_times = [time / 2 for time in response_times_ms]
print("Half times:", half_times)