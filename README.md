# Student Database Management System
## Overview
This project is a simple Python script for managing a PostgreSQL database containing student information. It provides basic operations such as adding, updating, and deleting student records.

## Requirements
- Python 3.x
- psycopg2
- PostgreSQL

## Setup
1. Install the required Python packages:

`pip install psycopg2`

2. Create a PostgreSQL database and run the SQL scripts provided in the sql directory to set up the necessary tables and initial data.

3. Modify the command-line arguments in main.py as needed to connect to your PostgreSQL database.

## Usage
Run the main.py script with the necessary command-line arguments:

`python main.py --password your_password --commit True`

## Available Operations
- `getAllStudents()`: Retrieves all student records from the database.
- `addStudent(first_name, last_name, email, enrollment_date)`: Adds a new student to the database.
- `updateStudentEmail(new_email, student_id)`: Updates the email address of an existing student.
- `deleteStudent(student_id)`: Deletes a student from the database.

## License
This project is licensed under the MIT License.
