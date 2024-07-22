import sqlite3
from faker import Faker
import random
from datetime import datetime

# Initialize Faker
fake = Faker()

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Create people table
cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    created_at TEXT,
    updated_at TEXT
)
''')

# Generate and insert 200 fake people
for _ in range(200):
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(1, 100)
    created_at = datetime.now().isoformat()
    updated_at = created_at

    cursor.execute('''
    INSERT INTO people (first_name, last_name, age, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, age, created_at, updated_at))

# Commit the transaction and close the connection
conn.commit()
conn.close()