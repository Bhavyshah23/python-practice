# Practical 3: Grade Calculator

maths = float(input("Enter your Maths Marks: "))
science = float(input("Enter your Science Marks: "))
english = float(input("Enter your English Marks: "))

total_marks = maths + science + english

percentage = (total_marks /300) * 100

if percentage >= 90:
    print("Your Grade is A")
elif percentage >= 75:
    print("Your Grade is B")
elif percentage >= 60:
    print("Your Grade is C")
elif percentage >= 50:
    print("Your Grade is D")
else:
    print("Your Grade is F")

