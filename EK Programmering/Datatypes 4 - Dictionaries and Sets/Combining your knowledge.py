#Combining your knowledge
#Now that you know the most common datatypes, it is time to put them all together!

#Make a program that does the following:

#1. Make an empty list called “first_list”

#2. Declare 3 number variables and add them to the list.

#3. Declare 3 strings and add them to the list.

#4. Make a new list called “second_list” that contains all the elements of “first_list” TWICE.

#5. Add “first_list” and “second_list” to a dictionary and give them appropriate keys.

#6. Delete any reference to “first_list” and “second_list” # first_list, second_list = None

#7. Using the dictionary, delete all the strings from the first key/value pair.

#8. Add a new key/value pair to the dictionary, the key should be “age” and the value should

#be your age.

#9. Print the full dictionary

#10. Print only your age from the dictionary.

#11. Print the first number of what used to be “second_list” from the dictionary. 

# 1. Empty list
first_list = []

# 2. Declare 3 numbers
num1 = 6
num2 = 9
num3 = 69

first_list.append(num1)
first_list.append(num2)
first_list.append(num3)

# 3. Declare 3 strings
str1 = "Sechs"
str2 = "Neun"
str3 = "Neunundsechzig"

first_list.append(str1)
first_list.append(str2)
first_list.append(str3)

print("First list:", first_list)

# 4. second_list contains elements twice
second_list = first_list * 2
print("Second list:", second_list)

# 5. Add both lists to dictionary
data = {
    "original": first_list,
    "double": second_list
}

print("Dictionary after adding lists:", data)

# 6. Delete references
first_list, second_list = None, None

# 7. Delete all strings from first key/value pair
data["original"] = [item for item in data["original"] if type(item) == int]

print("After removing strings:", data)

# 8. Add age
data["age"] = 26

# 9. Print full dictionary
print("Full dictionary:", data)

# 10. Print only age
print("Age:", data["age"])

# 11. Print first number of what used to be second_list
print("First number from double list:", data["double"][0])
