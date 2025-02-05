import sqlite3
import csv

# Database SQLite
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Creazione della tabella
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        year_of_birth INTEGER NOT NULL,
        gender TEXT NOT NULL,
        email TEXT NOT NULL,
        assignments INTEGER DEFAULT 0
    )
''')

# Lettura del CSV e inserimento dati
with open("students.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)  # Salta l'intestazione
    for row in reader:
        cursor.execute('''
            INSERT OR IGNORE INTO students (id, first_name, last_name, year_of_birth, gender, email, assignments)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (int(row[0]), row[1], row[2], int(row[3]), row[4], row[5], int(row[6])))

conn.commit()

# Stampa degli studenti nati nel 2000
print("\nStudenti nati nel 2000:")
cursor.execute("SELECT first_name, last_name FROM students WHERE year_of_birth = 2000")
for row in cursor.fetchall():
    print(row)

# Studente con il maggior numero di assignments
cursor.execute("SELECT first_name, last_name, MAX(assignments) FROM students")
max_assignments = cursor.fetchone()
print(f"\nStudente con più assignments: {max_assignments[0]} {max_assignments[1]}")

# Cognome delle studentesse di nome Jane
print("\nCognomi delle studentesse di nome Jane:")
cursor.execute("SELECT last_name FROM students WHERE first_name = 'Jane' AND gender = 'F'")
for row in cursor.fetchall():
    print(row[0])

# Graduatoria studenti ordinata per assignments
print("\nGraduatoria studenti (ordine assignments):")
cursor.execute("SELECT first_name, last_name, assignments FROM students ORDER BY assignments DESC")
for row in cursor.fetchall():
    print(row)

# Chiudi la connessione
conn.close()