# Task 4: Grade calculation with if, elif and else

marks = float(input("Enter marks (0 to 100): "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value from 0 to 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")
