#Make a script that asks for your age (input) and stores it in a variable. Give this variable an appropriate name. 
#The script should now do the following:

#1. Print how old you will be in 100 years.

#2. Print what the year will be, when you turn 100. Keep in mind that the current year is 2026

# Ask for the user's age
current_age = int(input("Enter your age: "))

# Fixed current year
current_year = 2026

# 1. Age in 100 years
age_in_100_years = current_age + 100
print("In 100 years, you will be", age_in_100_years, "years old.")

# 2. Year when the user turns 100
years_until_100 = 100 - current_age
year_turning_100 = current_year + years_until_100
print("You will turn 100 years old in the year", year_turning_100)
