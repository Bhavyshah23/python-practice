# Practical 2: Calculate the area of a rectangle (length = 10, width = 5). Print the result.
length = 10
width = 5

area = length * width

# Simple concatenation
print("The area of the rectangle is " + str(area) + ".")

print()  # Add a blank line for better readability

# Using f-strings (Python 3.6+)
print(f"The area of the rectangle is {area}.")

print()  # Add a blank line for better readability

# Using the format() method
print("The area of the rectangle is {}.".format(area))