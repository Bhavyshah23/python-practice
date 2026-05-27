# Write a Program to find the gratest of 4 numbers enter by the user.

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
num3 = float(input("Enter Third Number: "))
num4 = float(input("Enter Fourth Number: "))

if (num1 >= num2 and num1 >= num3 and num1 >= num4):
    print("First number is largest: ", num1)
elif (num2 >= num3 and num2 >= num4):
    print("The Second number is largest: ", num2)
elif (num3 >= num4):
    print("The Third number is largest: ", num3)
else:
    print("The Fourth number is largest: ", num4)