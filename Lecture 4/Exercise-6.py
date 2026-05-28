student_info = {
    "name" : "Bhavy",
    "age" : 21,
    "city" : "Ahmedabad",
    "favorite_subjects" : ["Maths", "Physics", "Chemistry"]
}

# Print the student's name and age together.
print(student_info["name"], student_info["age"])

# Add a new key "grade" with value "A".
student_info["grade"] = "A"
print(student_info)

print(student_info.keys())