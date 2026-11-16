
# Student Details Feature

def student_details():
    print("\n--- Student Details ---")

    name = input("Enter student name: ")
    usn = input("Enter student USN: ")
    department = input("Enter department: ")

    print("\nStudent Information")
    print("Name:", name)
    print("USN:", usn)
    print("Department:", department)

if __name__ == "__main__":
    student_details()
