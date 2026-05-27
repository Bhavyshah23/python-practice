# Practical 4: Convert temperature from Celsius to Fahrenheit (Formula: F = C * 9/5 + 32).

# Get user input for temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = celsius * 9/5 + 32

# Print the result

# Using f-strings (Python 3.6+)
print(f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
