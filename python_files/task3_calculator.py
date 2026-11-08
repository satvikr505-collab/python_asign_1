# Task 3: Calculator using arithmetic operators

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

print("\nCALCULATOR RESULT")
print("-" * 25)
print(f"Addition       : {first + second:g}")
print(f"Subtraction    : {first - second:g}")
print(f"Multiplication : {first * second:g}")

if second != 0:
    print(f"Division       : {first / second:g}")
    print(f"Modulus        : {first % second:g}")
else:
    print("Division       : not possible (division by zero)")
    print("Modulus        : not possible (division by zero)")
