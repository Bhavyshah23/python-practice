# Practical 6: Take data from user input for a person's name, age, and height. Then print the information in a formatted sentence.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print()  # Add a blank line for better readability

# Using f-strings (Python 3.6+)
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} meters tall.")
