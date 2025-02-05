import sqlite3
import csv

conn = sqlite3.connect("my.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")

cur.execute(
    '''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        quotaAmount INTEGER,
        month INTEGER,
        agent TEXT,
        username TEXT)''')

conn.commit()

with open("data.csv", encoding="utf-8") as fd:
    reader = csv.reader(fd)
    header = next(reader)

    for row in reader:
        cur.execute(
            "INSERT INTO users (quotaAmount, month, agent, username) VALUES (?, ?, ?, ?)",
            row
        )

conn.commit()

cur.execute("SELECT SUM(quotaAmount) FROM users WHERE month = 1")
total_january_sales = cur.fetchone()[0]
print(f"Giro d'affari complessivo di gennaio: {total_january_sales}")

cur.execute("SELECT MAX(quotaAmount), agent FROM users")
max_sales = cur.fetchone()
print(f"La vendita più redditizia è stata fatta da {max_sales[1]} con un importo di {max_sales[0]}")

cur.execute("SELECT SUM(quotaAmount) FROM users WHERE agent = 'Chris Riley'")
total_sales_chris = cur.fetchone()[0]
print(f"Giro d'affari complessivo di Chris Riley: {total_sales_chris}")

conn.close()
