# Task 1: Python Basics
# A simple introduction program using input() and print().

print("=" * 42)
print("       WELCOME TO PYTHON LEARNING")
print("=" * 42)

name = input("Enter your name: ").strip()
college = input("Enter your college name: ").strip()
branch = input("Enter your branch: ").strip()

print("\n--- Student Introduction ---")
print(f"Name          : {name}")
print(f"College       : {college}")
print(f"Branch        : {branch}")
print("\nGlad to have you here. Happy learning!")
