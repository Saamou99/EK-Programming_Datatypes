#Start your program with an empty dictionary called “book_prices”

#Your program must now do the following:

#1. Add three books and their prices (see table on the #right)

#2. Print out the price of “Mad Max”

#3. Access a book not in the dictionary using .get()

#4. Update the price of “Lord of the Rings” to 200

#5. Add a new book to the list of your choosing.

#6. Delete “Cybersikkerhed 101” from your dictionary.

#7. Do a check if “Cybersikkerhed 101” still exists

#8. Do a check if “Mad Max” still exists

#Between each step, it is recommended that you print the dictionary to keep track of your changes.

#The three books:

#"Lord of the Rings" : 150
#"Cybersikkerhed 101" : 500
#"Mad Max" : 399

# Start with empty dictionary
book_prices = {}

print("Step 1:", book_prices)

# 1. Add three books
book_prices["Lord of the Rings"] = 150
book_prices["Cybersikkerhed 101"] = 500
book_prices["Mad Max"] = 399

print("Step 2:", book_prices)

# 2. Print price of “Mad Max”
print("Price of Mad Max:", book_prices["Mad Max"])

# 3. Access book not in dictionary using .get()
print("Harry Potter:", book_prices.get("Harry Potter"))

# 4. Update price of “Lord of the Rings” to 200
book_prices["Lord of the Rings"] = 200
print("Step 4:", book_prices)

# 5. Add a new book
book_prices["Batman till the end"] = 169
print("Step 5:", book_prices)

# 6. Delete “Cybersikkerhed 101”
del book_prices["Cybersikkerhed 101"]
print("Step 6:", book_prices)

# 7. Check if “Cybersikkerhed 101” exists
print("Cybersikkerhed 101 exists:",
      "Cybersikkerhed 101" in book_prices)

# 8. Check if “Mad Max” exists
print("Mad Max exists:",
      "Mad Max" in book_prices)

print(book_prices)