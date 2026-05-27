# Practical 3: Take two numbers from user input and print their sum, difference, product, and division.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
division_result = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

print()  # Add a blank line for better readability

# Using f-strings (Python 3.6+)
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The difference between {num1} and {num2} is: {difference_result}")
print(f"The product of {num1} and {num2} is: {product_result}")
print(f"The division of {num1} by {num2} is: {division_result}")
