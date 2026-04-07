# 7.4: Create the list
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5: Capitalize the person (cinderella)
print(things[1].capitalize())
print(things)
# Answer: No, it did not change the element in the list. 
# String methods in Python return a new string and do not modify the original list element in-place.

# 7.6: Uppercase the cheesy element (mozzarella) and update the list
things[0] = things[0].upper()
print(things)

# 7.7: Delete the disease element (salmonella)
del things[-1]
print(things)


# 9.1: Define a function that returns a list
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

# 9.2: Define a generator function for odd numbers
def get_odds():
    for number in range(1, 10, 2):
        yield number

# Use a for loop to find and print the third value (1 is 1st, 3 is 2nd, 5 is 3rd)
count = 1
for number in get_odds():
    if count == 3:
        print(f"The third odd number is: {number}")
        break
    count += 1