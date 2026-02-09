#Declare a list as such:
#my_list = [0,1,2,3,4,5,6,7,8]

#Now make a program that does the following:

#1. Print the full list

#2. Print the first element of the list

#3. Print the last element of the list

#4. Print the first 4 elements

#5. Using “my_list”, declare a list called “second_list” and assign it the last 3 elements of “my_list” as its value.

# Declare the list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 1. Print the full list
print(my_list)

# 2. Print the first element
print(my_list[0])

# 3. Print the last element
print(my_list[-1])

# 4. Print the first 4 elements
print(my_list[:4])

# 5. Create a new list with the last 3 elements
second_list = my_list[-3:]
print(second_list)