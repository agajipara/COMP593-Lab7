import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Query the database for people aged 50 and above
cursor.execute('''
SELECT first_name, last_name, age
FROM people
WHERE age >= 50
''')

# Fetch all results
results = cursor.fetchall()

# Print results
for first_name, last_name, age in results:
    print(f"{first_name} {last_name} is {age} years old.")

# Save results to a CSV file
df = pd.DataFrame(results, columns=['First Name', 'Last Name', 'Age'])
df.to_csv('old_people.csv', index=False)

# Close the connection
conn.close()