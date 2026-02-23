#Make two variables called “first_name” and “last_name” and assign
#them appropriate values.

#Your program should now do the following things:

#1. Concatenate your two strings into one string. Give this new string an appropriate name for the
#sake of readability.

#2. Print your string.

#3. Print the length of your string.

#4. Print your string 50 times in row.

#5. Print ONLY the last character of your string.

#6. Make it look (search) for any “z” characters in your name, and have it print True or False whether it finds any of these characters.
###

#Variables:
first_name = "Saamou"
last_name = "Shakoor"

#Concatenate the strings
full_name = first_name + " " + last_name

#Print the full name
print(full_name)

#Print the length of the string
print(len(full_name))

#Print the string 69 times
print(full_name * 69)

#Print only the last character
print(full_name[-1])

#Check for the letter "z"
print("z" in full_name)

