import csv
import sqlite3
from datetime import datetime, timedelta
import random
import os

def create_csv_files():
    # Connessione al database students.db
    with sqlite3.connect('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

    # Scrivere students_no_assignments.csv
    with open('students_no_assignments.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["id", "first_name", "last_name", "year_of_birth", "gender", "email"])
        writer.writerows(students)

    # Generare e scrivere assignments.csv
    if not os.path.exists('assignments.csv'):  # Evita di sovrascrivere il file se esiste già
        with open('assignments.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["id", "student_id", "submission_date"])
            assignment_id = 1
            for student in students:
                for _ in range(random.randint(1, 5)):  # Numero casuale di assignments
                    submission_date = (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
                    writer.writerow([assignment_id, student[0], submission_date])
                    assignment_id += 1

def create_assignments_database():
    # Connessione al database assignments.db
    with sqlite3.connect('assignments.db') as conn:
        cursor = conn.cursor()

        # Creare le tabelle
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            year_of_birth INTEGER NOT NULL,
            gender TEXT NOT NULL,
            email TEXT NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            submission_date TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
        ''')

        # Svuotare le tabelle prima di inserire nuovi dati
        cursor.execute("DELETE FROM students")
        cursor.execute("DELETE FROM assignments")

        # Popolare la tabella students (ignorare i duplicati)
        with open('students_no_assignments.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                cursor.execute('''
                INSERT OR IGNORE INTO students (id, first_name, last_name, year_of_birth, gender, email)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (row['id'], row['first_name'], row['last_name'], row['year_of_birth'], row['gender'], row['email']))

        # Popolare la tabella assignments (ignorare i duplicati)
        with open('assignments.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                cursor.execute('''
                INSERT OR IGNORE INTO assignments (id, student_id, submission_date)
                VALUES (?, ?, ?)
                ''', (row['id'], row['student_id'], row['submission_date']))

def execute_queries():
    # Connessione al database assignments.db
    with sqlite3.connect('assignments.db') as conn:
        cursor = conn.cursor()

        # Query 1: Studenti nati nel 2000
        cursor.execute("SELECT first_name, last_name FROM students WHERE year_of_birth = 2000")
        print("Studenti nati nel 2000:")
        print(cursor.fetchall())

        # Query 2: Persona con il maggior numero di assignments
        cursor.execute('''
        SELECT s.first_name, s.last_name, COUNT(a.id) AS total_assignments
        FROM students s
        LEFT JOIN assignments a ON s.id = a.student_id
        GROUP BY s.id
        ORDER BY total_assignments DESC
        LIMIT 1
        ''')
        print("\nPersona con il maggior numero di assignments:")
        print(cursor.fetchone())

        # Query 3: Cognome delle studentesse di nome "Jane"
        cursor.execute("SELECT last_name FROM students WHERE first_name = 'Jane' AND gender = 'F'")
        print("\nCognome delle studentesse di nome Jane:")
        print([row[0] for row in cursor.fetchall()])

        # Query 4: Graduatoria degli studenti ordinati per numero di assignments
        cursor.execute('''
        SELECT s.first_name, s.last_name, COUNT(a.id) AS total_assignments
        FROM students s
        LEFT JOIN assignments a ON s.id = a.student_id
        GROUP BY s.id
        ORDER BY total_assignments DESC
        ''')
        print("\nGraduatoria degli studenti ordinati per numero di assignments:")
        print(cursor.fetchall())

def main():
    # Creazione dei file CSV a partire dal database students.db
    create_csv_files()

    # Creazione e popolamento del database bonus
    create_assignments_database()

    # Esecuzione delle query richieste
    execute_queries()

# Esecuzione del programma
if __name__ == "__main__":
    main()