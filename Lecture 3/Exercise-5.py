# Mixed Challenge

num1 = float(input("Enter First number:"))
num2 = float(input("Enter Second number:"))
num3 = float(input("Enter Third number:"))
num4 = float(input("Enter Fourth number:"))
num5 = float(input("Enter Fifth number:"))

numbers = [num1, num2, num3, num4, num5]

sum_numbers = sum(numbers)
print(f"The sum of the numbers is: {sum_numbers}")

avg_number = sum_numbers / len(numbers)
print(f"The average of the numbers is: {avg_number}")

max_number = max(numbers)
min_number = min(numbers)
print(f"The maximum number is: {max_number}")
print(f"The minimum number is: {min_number}")