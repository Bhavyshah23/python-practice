# Set + Dictionary (Easier Version)

# Take 3 subject names as input from the user and store them in a Set (to avoid duplicates).
subjects = set()

# Take 3 subject names
sub1 = input("Enter subject 1 name: ")
subjects.add(sub1)

sub2 = input("Enter subject 2 name: ")
subjects.add(sub2)

sub3 = input("Enter subject 3 name: ")
subjects.add(sub3)

# Take marks for each subject
marks_dict = {}

marks_dict[sub1] = float(input(f"Enter marks for {sub1}: "))
marks_dict[sub2] = float(input(f"Enter marks for {sub2}: "))
marks_dict[sub3] = float(input(f"Enter marks for {sub3}: "))

# Output
print("\nSubjects and Marks:", marks_dict)

average = sum(marks_dict.values()) / len(marks_dict)
print(f"Average Marks: {average:.2f}")