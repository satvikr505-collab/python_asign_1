# Task 5: for loop, multiplication table and while loop

print("Numbers from 1 to 20:")
for number in range(1, 21):
    print(number, end=" ")
print("\n")

table_number = int(input("Enter a number for its multiplication table: "))
print(f"\nTable of {table_number}:")
for multiplier in range(1, 11):
    print(f"{table_number} x {multiplier} = {table_number * multiplier}")

print("\nEven numbers from 1 to 50:")
number = 2
while number <= 50:
    print(number, end=" ")
    number += 2
print()
