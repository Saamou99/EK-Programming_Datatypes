#Declare a variable called "full_name" and give it an appropriate value.
#Make a program that can do the following:

#1. Make a list from the string, where each element is a part of your name. Element 0 should be your first name, element 1 your middle name etc. Give the list an appropriate name.

#2. Print out the list.

#3. Prove that your new list is actually a list type.

#4. Make another new list from your "full_name" string, this time splitting on the “a” character. Print the new list and take a note of what happens.

#5. Finally, put your list back together into a new string. Name this string "full_name_restored”

# Step 1: Declare the full name
full_name = "Saim Shakoor Nadeem"

# Step 2: Split the name into parts (by space)
name_parts = full_name.split(" ")

# Step 3: Print the list
print(name_parts)

# Step 4: Prove it is a list
print(type(name_parts))

# Step 5: Split the name using the letter "a"
split_on_a = full_name.split("a")
print(split_on_a)

# Step 6: Restore the name from the original list
full_name_restored = " ".join(name_parts)
print(full_name_restored)
