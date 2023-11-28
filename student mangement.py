K**o, [11/28/2023 9:32 AM]
# Define a dictionary to store the student database
student_db = {}

# Define a function to add a new student to the database
def add_student():
    # Ask the user to enter the name, age, grade, and any other details of the new student
    name = input("Enter the name of the new student: ")
    age = int(input("Enter the age of the new student: "))
    grade = input("Enter the grade of the new student: ")
    details = input("Enter any other details of the new student (separated by commas): ")

    # Create a dictionary to store the information of the new student
    student_info = {
        "name": name,
        "age": age,
        "grade": grade,
        "details": details.split(",")
    }

    # Add the new student to the database using the name as the key
    student_db[name] = student_info

    # Print a confirmation message
    print(f"Successfully added {name} to the database.")

# Define a function to view the details of a specific student by entering the student's name
def view_student():
    # Ask the user to enter the name of the student they want to view
    name = input("Enter the name of the student you want to view: ")

    # Check if the student exists in the database
    if name in student_db:
        # Retrieve the student information from the database
        student_info = student_db[name]

        # Print the student information
        print(f"Name: {student_info['name']}")
        print(f"Age: {student_info['age']}")
        print(f"Grade: {student_info['grade']}")
        print(f"Details: {', '.join(student_info['details'])}")
    else:
        # Print an error message
        print(f"Sorry, there is no student with the name {name} in the database.")

# Define a function to display a list of all students in the database with their basic information
def list_all_students():
    # Check if the database is empty
    if student_db:
        # Print a header
        print("List of all students in the database:")

        # Loop through the database and print each student's basic information
        for name, student_info in student_db.items():
            print(f"Name: {name}, Age: {student_info['age']}, Grade: {student_info['grade']}")
    else:
        # Print a message
        print("The database is empty. Please add some students first.")

# Define a function to update the information of a specific student, such as changing their grade or age
def update_student():
    # Ask the user to enter the name of the student they want to update
    name = input("Enter the name of the student you want to update: ")

    # Check if the student exists in the database
    if name in student_db:
        # Retrieve the student information from the database
        student_info = student_db[name]

        # Print the current student information
        print(f"Current information of {name}:")
        print(f"Name: {student_info['name']}")
        print(f"Age: {student_info['age']}")
        print(f"Grade: {student_info['grade']}")
        print(f"Details: {', '.join(student_info['details'])}")

        # Ask the user what they want to update
        print("What do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Grade")
        print("4. Details")
        print("5. Cancel")

        # Get the user's choice
        choice = int(input("Enter your choice (1-5): "))

        # Validate the user's choice
        if choice == 1:
            # Ask the user to enter the new name
            new_name = input("Enter the new name: ")

            # Update the name in the database
            student_db[new_name] = student_db.pop(name)

            # Print a confirmation message
            print(f"Successfully updated the name of {name} to {new_name}.")
        elif choice == 2:
            # Ask the user to enter the new age
            new_age = int(input("Enter the new age: "))

            # Update the age in the database
            student_db[name]['age'] = new_age

K**o, [11/28/2023 9:32 AM]
# Print a confirmation message
            print(f"Successfully updated the age of {name} to {new_age}.")
        elif choice == 3:
            # Ask the user to enter the new grade
            new_grade = input("Enter the new grade: ")

            # Update the grade in the database
            student_db[name]['grade'] = new_grade

            # Print a confirmation message
            print(f"Successfully updated the grade of {name} to {new_grade}.")
        elif choice == 4:
            # Ask the user to enter the new details
            new_details = input("Enter the new details (separated by commas): ")

            # Update the details in the database
            student_db[name]['details'] = new_details.split(",")

            # Print a confirmation message
            print(f"Successfully updated the details of {name} to {new_details}.")
        elif choice == 5:
            # Print a message
            print("No changes made.")
        else:
            # Print an error message
            print("Invalid choice. Please enter a number between 1 and 5.")
    else:
        # Print an error message
        print(f"Sorry, there is no student with the name {name} in the database.")

# Define a function to delete a student from the database based on their name
def delete_student():
    # Ask the user to enter the name of the student they want to delete
    name = input("Enter the name of the student you want to delete: ")

    # Check if the student exists in the database
    if name in student_db:
        # Delete the student from the database
        student_db.pop(name)

        # Print a confirmation message
        print(f"Successfully deleted {name} from the database.")
    else:
        # Print an error message
        print(f"Sorry, there is no student with the name {name} in the database.")

# Define a function to display the main menu and get the user's choice
def main_menu():
    # Print the main menu
    print("Welcome to the student database program.")
    print("Please choose an action:")
    print("1. Add a new student")
    print("2. View a specific student")
    print("3. List all students")
    print("4. Update a student's information")
    print("5. Delete a student")
    print("6. Exit")

    # Get the user's choice
    choice = int(input("Enter your choice (1-6): "))

    # Return the user's choice
    return choice

# Define the main function to run the program
def main():
    # Loop until the user chooses to exit
    while True:
        # Get the user's choice from the main menu
        choice = main_menu()

        # Perform the corresponding action based on the user's choice
        if choice == 1:
            # Add a new student
            add_student()
        elif choice == 2:
            # View a specific student
            view_student()
        elif choice == 3:
            # List all students
            list_all_students()
        elif choice == 4:
            # Update a student's information
            update_student()
        elif choice == 5:
            # Delete a student
            delete_student()
        elif choice == 6:
            # Exit the program
            print("Thank you for using the student database program. Goodbye.")
            break
        else:
            # Print an error message
            print("Invalid choice. Please enter a number between 1 and 6.")

        # Print a blank line
        print()

# Call the main function to run the program
main()