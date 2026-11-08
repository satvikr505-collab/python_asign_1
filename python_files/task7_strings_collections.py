# Task 7: Strings and Python collections

# String methods
message = "Python makes data work easier"
print("Original string:", message)
print("upper():", message.upper())
print("lower():", message.lower())
print("replace():", message.replace("easier", "interesting"))
print("find('data'):", message.find("data"))

# List methods
subjects = ["Python", "Networks", "C"]
subjects.append("Statistics")
subjects.remove("C")
subjects.sort()
print("\nList after append, remove and sort:", subjects)

# Tuple and indexing
coordinates = (12, 25, 38)
print("\nTuple:", coordinates)
print("Item at index 1:", coordinates[1])

# Dictionary
student = {
    "name": "Satvik Rai",
    "programme": "MCA",
    "semester": 1
}
print("\nStudent dictionary:", student)
print("Student name:", student["name"])

# Set operations
skills = {"Python", "SQL", "Excel"}
skills.add("Power BI")
skills.remove("Excel")
print("\nSet after add() and remove():", sorted(skills))
