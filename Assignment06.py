# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: A program that registers students for courses, demonstrating the use of functions,
#       classes, and error handling.
# Change Log: (Who, When, What)
#   RRoot, 1/1/2030, Created Script
#   Tony Fernandez, 11/20/2024, Modified script to include classes and functions
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
# Define the Data Constants
#FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = '' # Hold the choice made by the user.

# Class Definitions

class FileProcessor:
    """Processes data to and from a file and a list of dictionaries"""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a file into a list of dictionary rows"""
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                student_data.extend(data)
        except FileNotFoundError:
            print(f"{file_name} not found. Starting with an empty list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {file_name}. Starting with an empty list.")
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with reading the file.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes data from a list of dictionary rows to a file"""
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file, indent=4)
            print("The following data was saved to file!")
            IO.output_student_courses(student_data)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)

#Other thingy
class IO:
    """Performs Input and Output tasks"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays error messages to the user"""
        print(message)
        if error:
            print("-- Technical Error Message --")
            print(error)

    @staticmethod
    def output_menu(menu: str):
        """Displays the menu to the user"""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Gets the menu choice from the user"""
        return input("Enter Number Here: ").strip()

    @staticmethod
    def input_student_data(student_data: list):
        """Gets student data from the user and adds it to the list"""
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ").strip()
            if not course_name:
                raise ValueError("Course name cannot be empty.")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays current student registrations"""
        if not student_data:
            print("No student registrations found.")
        else:
            print("-" * 50)
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-" * 50)

if __name__ == "__main__":
    # When the program starts, read the file data into a list of dictionaries
    FileProcessor.read_data_from_file(FILE_NAME, students)

    # Present and Process the data
    while True:
        # Present the menu of choices
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        # Input user data
        if menu_choice == "1":  # Register a student
            IO.input_student_data(students)
            continue

        # Present the current data
        elif menu_choice == "2":
            IO.output_student_courses(students)
            continue

        # Save the data to a file
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
            continue

        # Stop the loop
        elif menu_choice == "4":
            print("Program Ended")
            break  # out of the loop

        else:
            IO.output_error_messages("Please only choose option 1, 2, 3, or 4")
print("Program Ended")
