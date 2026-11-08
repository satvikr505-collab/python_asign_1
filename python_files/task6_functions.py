# Task 6: User-defined functions

def square(number):
    """Return the square of the supplied number."""
    return number * number


def average(first, second, third):
    """Return the arithmetic mean of three numbers."""
    return (first + second + third) / 3


value = float(input("Enter a number to find its square: "))
print(f"Square of {value:g} = {square(value):g}")

print("\nEnter three numbers to calculate their average.")
a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))
print(f"Average = {average(a, b, c):g}")
