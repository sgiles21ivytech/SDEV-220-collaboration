import sqlite3
import sqlalchemy as sa
import pandas as pd

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS books (
  title TEXT,
  author TEXT,
  year INTEGER
);
"""

cursor.execute(create_table_query)
conn.commit()
conn.close()
print("Database and table created successfully!")

"""Database connection phase"""
engine = sa.create_engine('sqlite:///books.db')

# Reading Data Phase
df = pd.read_csv('books2.csv')
df.to_sql('book', engine, if_exists='append', index=False)

# Sucess Message
print("Data inserted successfully!")

