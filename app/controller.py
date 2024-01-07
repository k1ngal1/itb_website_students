from db import obtain_connection

# Define controls (CRUD)


def insert_students(passport, name, birth, height):
    connection = obtain_connection()
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO students(passport,name, birth, height) VALUES (%s, %s, %s, %s)",
                       (passport, name, birth, height))
    connection.commit()
    connection.close()


def obtain_student():
    connection = obtain_connection()
    students = []
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT passport, name, birth, height FROM students ORDER BY name")
        students = cursor.fetchall()
    connection.close()
    return students


def delete_student(passport):
    connection = obtain_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM students WHERE passport = %s", (passport,))
    connection.commit()
    connection.close()


def obtain_student_from_passport(passport):
    connection = obtain_connection()
    student = None
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT passport, name, birth, height FROM students WHERE passport = %s", (passport,))
        student = cursor.fetchone()
    connection.close()
    return student


def update_student(name, birth, height, passport):
    connection = obtain_connection()
    with connection.cursor() as cursor:
        cursor.execute("UPDATE students SET name = %s, birth = %s, height = %s WHERE passport = %s",
                       (name, birth, height, passport))
    connection.commit()
    connection.close()
