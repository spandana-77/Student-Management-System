
# Student Dashboard Feature

def dashboard():
    print("\n===== STUDENT DASHBOARD =====")
    print("1. View Profile")
    print("2. View Attendance")
    print("3. View Results")
    print("4. Logout")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Opening Student Profile...")
    elif choice == "2":
        print("Displaying Attendance...")
    elif choice == "3":
        print("Displaying Results...")
    elif choice == "4":
        print("Logged out successfully!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    dashboard()
