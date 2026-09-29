from validation import get_positive_integer, get_non_empty_text, find_by_id


def add_student(students):
    print("\n--- Add Student ---")
    student_id = get_positive_integer("Enter student ID: ")

    if find_by_id(students, student_id) is not None:
        print("A student with this ID already exists.")
        return

    name = get_non_empty_text("Enter student name: ")
    course = get_non_empty_text("Enter course: ")

    student = {
        "id": student_id,
        "name": name,
        "course": course
    }

    students.append(student)
    print("Student added successfully.")


def view_students(students):
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No students registered.")
        return

    for student in students:
        print(
            "ID:", student["id"],
            "| Name:", student["name"],
            "| Course:", student["course"]
        )
