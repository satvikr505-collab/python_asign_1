# Task 9: Student Record Management System
# Records are stored in a list of dictionaries while the program runs.

students = []


def add_student():
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    course = input("Enter course: ").strip()

    if not name or not roll_no or not course:
        print("All fields are required. Record was not added.")
        return

    if any(student["roll_no"].lower() == roll_no.lower()
           for student in students):
        print("That roll number already exists.")
        return

    students.append({
        "name": name,
        "roll_no": roll_no,
        "course": course
    })
    print("Student record added successfully.")


def display_students():
    if not students:
        print("No student records are available.")
        return

    print("\nSTUDENT RECORDS")
    print("-" * 52)
    for student in students:
        print(
            f"Name: {student['name']} | "
            f"Roll No: {student['roll_no']} | "
            f"Course: {student['course']}"
        )


def search_student():
    search_name = input("Enter the name to search: ").strip().casefold()
    matches = [
        student for student in students
        if search_name in student["name"].casefold()
    ]

    if matches:
        print(f"\nFound {len(matches)} matching record(s):")
        for student in matches:
            print(
                f"Name: {student['name']} | "
                f"Roll No: {student['roll_no']} | "
                f"Course: {student['course']}"
            )
    else:
        print("No matching student was found.")


def delete_student():
    roll_no = input("Enter the roll number to delete: ").strip()
    for student in students:
        if student["roll_no"].lower() == roll_no.lower():
            students.remove(student)
            print("Student record deleted.")
            return
    print("No record found with that roll number.")


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGEMENT =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student by name")
        print("4. Delete student by roll number")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you for using the Student Record System.")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()
