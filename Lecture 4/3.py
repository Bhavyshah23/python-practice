# Write a program to enter marks of 3 subjects and store them in a dictionary.
# Starts with an empty dictionary & add one by one. Use subject name as key and marks as value. Finally print the dictionary.

marks = {}

Maths = int(input("Enter marks for Maths: "))
marks.update({"Maths" : Maths})

Physics = int(input("Enter marks for Physics: "))
marks.update({"Physics" : Physics})

Chemistry = int(input("Enter marks for Chemistry: "))
marks.update({"Chemistry" : Chemistry})


print(marks)
