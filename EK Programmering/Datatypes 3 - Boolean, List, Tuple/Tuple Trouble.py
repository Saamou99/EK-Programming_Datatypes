#Start by declaring a tuple as such:
#x = (1,2,3,4,5, "Sebastian")

#You realise that the teachers forgot to add the value "Alex" to the tuple. 
# It’s up to you to make a program that adds this value to the tuple, despite the fact that tuples don’t have an “append” method. 
# You have to add the value without hardcoding a new tuple 
# so you end up with a tuple that looks like this:
#(1,2,3,4,5, "Sebastian", "Alex")

# Original tuple
x = (1, 2, 3, 4, 5, "Sebastian")

# Add "Alex" by concatenating a single-element tuple
x = x + ("Alex",)

# Print the new tuple
print(x)