# Student Course Management System - SQL Relational Database Application


# Overview

I created this project to learn how relational databases work and how applications communicate with databases using SQL. Throughout this project, I practiced designing a database structure, creating relationships between tables, and performing CRUD operations using SQL queries.

This software is a Student Course Management System that allows users to manage student information, courses, and course enrollments. The application stores data permanently using a relational database instead of only keeping information while the program is running.

The database was designed using three main tables: Students, Courses, and Enrollments. These tables demonstrate the use of primary keys, foreign keys, and relationships between different types of information.

The purpose of this project is to gain experience with SQL relational databases, understand how data is organized, practice writing SQL queries, and learn how software applications interact with stored data.

[Software Demo Video](Im_Doing_the_video)


# Application Features

- Add new students
- View student records
- Delete student records
- Add new courses
- View available courses
- Enroll students into courses
- Display students and their courses using SQL JOIN queries
- Store information permanently using a relational database
- Use primary keys and foreign keys to maintain relationships between tables
- Perform CRUD operations with SQL queries


# Development Environment


## Tools Used

- Visual Studio Code
- Python 3
- SQLite
- Git
- GitHub


## Programming Language

- Python
- SQL


# Database Structure


The application uses a relational database with three main tables:


## Students Table

Stores information about students.

Columns:

- student_id (Primary Key)
- first_name
- last_name
- email


## Courses Table

Stores information about available courses.

Columns:

- course_id (Primary Key)
- course_name
- credits


## Enrollments Table

Creates a relationship between students and courses.

Columns:

- enrollment_id (Primary Key)
- student_id (Foreign Key)
- course_id (Foreign Key)


# Project Structure


- **main.py** – Contains the application menu and user interaction.
- **database.py** – Handles database creation, SQL queries, and CRUD operations.
- **student_course.db** – SQLite relational database file.
- **README.md** – Documentation explaining the project.


# How to Run the Application


1. Install Python 3.

2. Clone the repository.

3. Open the project folder.

4. Run the application using:
