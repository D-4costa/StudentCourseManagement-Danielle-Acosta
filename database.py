import sqlite3

DATABASE = "student_course.db"


# Creates a connection with the SQLite database
def connect():
    return sqlite3.connect(DATABASE)


# Creates all relational database tables
def create_tables():

    connection = connect()
    cursor = connection.cursor()


    # Students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)


    # Courses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses(
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL,
        credits INTEGER NOT NULL
    )
    """)


    # Enrollment relationship table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments(
        enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,

        FOREIGN KEY(student_id)
        REFERENCES Students(student_id),

        FOREIGN KEY(course_id)
        REFERENCES Courses(course_id)
    )
    """)


    connection.commit()
    connection.close()



# =====================================================
# STUDENT CRUD OPERATIONS
# =====================================================


# CREATE - Add a new student
def add_student(first_name, last_name, email):

    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO Students(first_name,last_name,email)
    VALUES(?,?,?)
    """,
    (first_name,last_name,email))


    connection.commit()
    connection.close()



# READ - Get all students
def get_students():

    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM Students
    """)

    students = cursor.fetchall()

    connection.close()

    return students



# UPDATE - Edit student information
def update_student(student_id, first_name, last_name, email):

    connection = connect()
    cursor = connection.cursor()


    cursor.execute("""
    UPDATE Students

    SET first_name=?,
        last_name=?,
        email=?

    WHERE student_id=?
    """,
    (
        first_name,
        last_name,
        email,
        student_id
    ))


    connection.commit()
    connection.close()



# DELETE - Remove student
def delete_student(student_id):

    connection = connect()
    cursor = connection.cursor()


    # Delete enrollments first because of foreign key relationship
    cursor.execute("""
    DELETE FROM Enrollments
    WHERE student_id=?
    """,
    (student_id,))


    cursor.execute("""
    DELETE FROM Students
    WHERE student_id=?
    """,
    (student_id,))


    connection.commit()
    connection.close()



# =====================================================
# COURSE CRUD OPERATIONS
# =====================================================


# CREATE - Add course
def add_course(course_name, credits):

    connection = connect()
    cursor = connection.cursor()


    cursor.execute("""
    INSERT INTO Courses(course_name,credits)
    VALUES(?,?)
    """,
    (
        course_name,
        credits
    ))


    connection.commit()
    connection.close()



# READ - Get courses
def get_courses():

    connection = connect()
    cursor = connection.cursor()


    cursor.execute("""
    SELECT *
    FROM Courses
    """)


    courses = cursor.fetchall()

    connection.close()

    return courses



# UPDATE - Edit course
def update_course(course_id, course_name, credits):

    connection = connect()
    cursor = connection.cursor()


    cursor.execute("""
    UPDATE Courses

    SET course_name=?,
        credits=?

    WHERE course_id=?
    """,
    (
        course_name,
        credits,
        course_id
    ))


    connection.commit()
    connection.close()



# DELETE - Remove course
def delete_course(course_id):

    connection = connect()
    cursor = connection.cursor()


    cursor.execute("""
    DELETE FROM Enrollments
    WHERE course_id=?
    """,
    (course_id,))


    cursor.execute("""
    DELETE FROM Courses
    WHERE course_id=?
    """,
    (course_id,))


    connection.commit()
    connection.close()



# =====================================================
# ENROLLMENT RELATIONSHIP
# =====================================================


# CREATE enrollment relationship
def enroll_student(student_id, course_id):

    connection = connect()
    cursor = connection.cursor()


    cursor.execute("""
    INSERT INTO Enrollments(student_id,course_id)
    VALUES(?,?)
    """,
    (
        student_id,
        course_id
    ))


    connection.commit()
    connection.close()



# READ using SQL JOIN
def get_student_courses():

    connection = connect()
    cursor = connection.cursor()


    cursor.execute("""
    SELECT

        Students.first_name,
        Students.last_name,

        Courses.course_name,
        Courses.credits


    FROM Enrollments


    JOIN Students

    ON Enrollments.student_id =
       Students.student_id


    JOIN Courses

    ON Enrollments.course_id =
       Courses.course_id

    """)


    data = cursor.fetchall()


    connection.close()

    return data