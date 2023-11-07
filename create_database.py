import sqlite3

# Connect to or create an SQLite database (if it doesn't exist, a new database file will be created)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define an SQL command to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS IpoData (
    id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Type TEXT,
    GMP TEXT,
    Price TEXT,
    Gain TEXT,
    Duration TEXT
);
"""

# Execute the SQL command to create the table
cursor.execute(create_table_query)

# Commit the changes and close the database connection
conn.commit()
conn.close()
