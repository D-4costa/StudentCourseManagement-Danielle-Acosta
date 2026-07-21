import database


# Main function that controls the application menu
# It creates the database tables first and then allows
# the user to interact with the Student Course Management System
def menu():

    # Creates Students, Courses, and Enrollments tables
    # if they do not already exist
    database.create_tables()


    while True:

        print("\n==============================")
        print(" Student Course Management")
        print("==============================")

        # Main menu options for database operations
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")

        print("5. Add Course")
        print("6. View Courses")
        print("7. Update Course")
        print("8. Delete Course")

        print("9. Enroll Student")
        print("10. View Student Courses")

        print("11. Exit")


        option = input("\nChoose an option: ")



        # ==========================
        # STUDENT MANAGEMENT
        # ==========================


        # Creates a new student record in the Students table
        if option == "1":

            first = input("First name: ")
            last = input("Last name: ")
            email = input("Email: ")


            database.add_student(
                first,
                last,
                email
            )


            print("Student added successfully!")



        # Retrieves and displays all students
        # using a SELECT SQL query
        elif option == "2":

            students = database.get_students()


            print("\nStudents:")

            for student in students:
                print(student)



        # Updates an existing student record
        # using an SQL UPDATE query
        elif option == "3":

            student_id = int(
                input("Student ID: ")
            )

            first = input("New first name: ")
            last = input("New last name: ")
            email = input("New email: ")


            database.update_student(
                student_id,
                first,
                last,
                email
            )


            print("Student updated successfully!")



        # Deletes a student record from the database
        # The related enrollments are removed first
        # to maintain the table relationship
        elif option == "4":

            student_id = int(
                input("Student ID to delete: ")
            )


            database.delete_student(student_id)


            print("Student deleted!")



        # ==========================
        # COURSE MANAGEMENT
        # ==========================


        # Creates a new course record
        # in the Courses database table
        elif option == "5":

            name = input("Course name: ")

            credits = int(
                input("Credits: ")
            )


            database.add_course(
                name,
                credits
            )


            print("Course added successfully!")



        # Displays all available courses
        # using a SELECT SQL query
        elif option == "6":

            courses = database.get_courses()


            print("\nCourses:")

            for course in courses:
                print(course)



        # Updates an existing course record
        elif option == "7":

            course_id = int(
                input("Course ID: ")
            )


            name = input("New course name: ")

            credits = int(
                input("New credits: ")
            )


            database.update_course(
                course_id,
                name,
                credits
            )


            print("Course updated successfully!")



        # Deletes a course and its enrollments
        # from the relational database
        elif option == "8":

            course_id = int(
                input("Course ID to delete: ")
            )


            database.delete_course(course_id)


            print("Course deleted!")



        # ==========================
        # ENROLLMENT MANAGEMENT
        # ==========================


        # Creates a relationship between a student
        # and a course using the Enrollments table
        elif option == "9":

            student = int(
                input("Student ID: ")
            )

            course = int(
                input("Course ID: ")
            )


            database.enroll_student(
                student,
                course
            )


            print("Enrollment completed!")



        # Displays combined information from
        # Students and Courses tables using SQL JOIN
        elif option == "10":

            courses = database.get_student_courses()


            print("\nStudent Courses:")


            for item in courses:

                print(
                    f"{item[0]} {item[1]} - "
                    f"{item[2]} "
                    f"({item[3]} credits)"
                )



        # Ends the application
        elif option == "11":

            print("Goodbye!")
            break



        else:

            print("Invalid option")



# Runs the program only when this file is executed directly
if __name__ == "__main__":
    menu()