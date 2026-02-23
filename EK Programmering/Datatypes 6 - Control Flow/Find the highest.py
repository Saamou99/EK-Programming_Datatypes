#Find the highest || #a = 1 #b = 2 #c = 3 || #Using only if sentences. 
#Find the highest number no matter which of the three variables has the highest one. 
#These operators are allowed: == , <, >, and, or, !=

# The data:
a = 1
b = 2
c = 3

if a > b and a > c:
    print("Highest number is:", a)

if b > a and b > c:
    print("Highest number is:", b)

if c > a and c > b:
    print("Highest number is:", c)