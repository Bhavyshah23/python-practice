# Mixed Challenge (Dictionary + Set)

# Take 5 subject names as input from the user and store them in a set (to remove duplicates).
subjects = set()
subject1 = int(input("Enter marks for subject 1: "))
subjects.add(subject1)
subject2 = int(input("Enter marks for subject 2: "))
subjects.add(subject2)
subject3 = int(input("Enter marks for subject 3: "))
subjects.add(subject3)
subject4 = int(input("Enter marks for subject 4: "))
subjects.add(subject4)
subject5 = int(input("Enter marks for subject 5: "))
subjects.add(subject5)


# Step 2: Create dictionary and take marks
marks_dict = {}
marks_dict["subject1"] = subject1
marks_dict["subject2"] = subject2
marks_dict["subject3"] = subject3
marks_dict["subject4"] = subject4
marks_dict["subject5"] = subject5

# Step 3: Print dictionary and average
print("nSubjects and Marks:", marks_dict)


# Calculate average

average = sum(subjects) / len(subjects)
print("Average Marks:", average)
