# Student Course Management System - SQL Relational Database Application

# Overview

I created this project to learn how relational databases work and how applications communicate with databases using SQL. Throughout this project, I practiced designing a database structure, creating relationships between tables, and performing CRUD operations using SQL queries.

This software is a Student Course Management System that allows users to manage student information, courses, and course enrollments. The application stores data permanently using a relational database instead of only keeping information while the program is running.

The database was designed using three main tables: Students, Courses, and Enrollments. These tables demonstrate the use of primary keys, foreign keys, and relationships between different types of information.

The purpose of this project is to gain experience with SQL relational databases, understand how data is organized, practice writing SQL queries, and learn how software applications interact with stored data.

**[Software Demo Video](https://youtu.be/zBwdsanFJ5E)**

# Application Features

- Add new students
- View student records
- Update student records
- Delete student records
- Add new courses
- View available courses
- Update course records
- Delete course records
- Enroll students in courses
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

## Programming Languages

- Python
- SQL

# Database Structure

The application uses a relational database with three main tables:

## Students Table

Stores information about students.

Columns:

- `student_id` (Primary Key)
- `first_name`
- `last_name`
- `email`

## Courses Table

Stores information about available courses.

Columns:

- `course_id` (Primary Key)
- `course_name`
- `credits`

## Enrollments Table

Creates a relationship between students and courses.

Columns:

- `enrollment_id` (Primary Key)
- `student_id` (Foreign Key)
- `course_id` (Foreign Key)

# Project Structure

- **main.py** – Contains the application menu and user interaction.
- **database.py** – Creates the database, manages SQL queries, and implements CRUD operations.
- **student_course.db** – SQLite relational database file.
- **README.md** – Project documentation.

# How to Run the Application

1. Install Python 3.
2. Clone this repository.
3. Open the project folder.
4. Run the application using:

```bash
python main.py
```

# Future Work

Some improvements I would like to make include:

- Add an option to search students by name.
- Add validation to prevent duplicate enrollments.
- Generate reports using SQL aggregate functions.
- Create a graphical user interface instead of a console application.
- Add instructor and classroom tables to expand the database.

# Useful Websites

- https://learn.microsoft.com/sql
- https://www.sqlite.org/docs.html
- https://docs.python.org/3/library/sqlite3.html
- https://code.visualstudio.com/docs
- https://github.com/
