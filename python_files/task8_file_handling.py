# Task 8: Creating, writing and reading a text file

introduction = (
    "Hello! My name is Satvik Rai.\\n"
    "I am pursuing MCA at Rajiv Gandhi University.\\n"
    "I am learning Python fundamentals for data analytics.\\n"
)

file_name = "student_introduction.txt"

# The with statement closes the file automatically.
with open(file_name, "w", encoding="utf-8") as file:
    file.write(introduction)

print(f"Introduction written to '{file_name}'.")

with open(file_name, "r", encoding="utf-8") as file:
    contents = file.read()

print("\\nContents read from the file:")
print("-" * 32)
print(contents, end="")
