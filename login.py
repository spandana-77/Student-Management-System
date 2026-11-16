
# Student Login Feature

def student_login():
    print("\n--- Student Login ---")

    email = input("Enter email: ")
    password = input("Enter password: ")

    if email and password:
        print("Login successful!")
    else:
        print("Please enter valid details.")

if __name__ == "__main__":
    student_login()
