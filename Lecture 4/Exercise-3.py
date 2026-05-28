# # Nested Dictionary

classroom = {
    "student1": {"name": "Aman", "marks": 92},
    "student2": {"name": "Priya", "marks": 88}
}

# # Name and marks of student1
# print(classroom["student1"]["name"], classroom["student1"]["marks"])

# # Name and marks of student2
# print(classroom["student2"]["name"], classroom["student2"]["marks"])

# Exercise 3: Nested Dictionary

classroom = {
    "student1": {"name": "Aman", "marks": 92},
    "student2": {"name": "Priya", "marks": 88}
}

# Print student1 details
print("Student 1:")
print("Name:", classroom["student1"]["name"])
print("Marks:", classroom["student1"]["marks"])

print("\nStudent 2:")   # \n creates a blank line
print("Name:", classroom["student2"]["name"])
print("Marks:", classroom["student2"]["marks"])