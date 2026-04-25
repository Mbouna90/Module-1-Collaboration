# ==========================================
# EXERCISE 11.1
# ==========================================
# Task: Create zoo.py and call hours()

# First, we create the zoo.py module file.
with open('zoo.py', 'w') as f:
    f.write("def hours():\n")
    f.write("    print('Open 9-5 daily')\n")

import zoo
print("Result of 11.1:")
zoo.hours()
print("-" * 30)

#==========================================
# EXERCISE 11.2
# ==========================================
# Task: Import zoo as menagerie

# 
# let's import the same module using an alias and call the function.
import zoo as menagerie
print("Result of 11.2:")
menagerie.hours()
print("-" * 30)


 #==========================================
# EXERCISE 16.8
# ==========================================
# Use SQLAlchemy to select titles from books.db alphabetically

# First, we must ensure books.db and the table exist (from 16.4/16.5).
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, select

# Setup: Creating the database and table so SQLAlchemy has something to read
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('DROP TABLE IF EXISTS books')
curs.execute('CREATE TABLE books (title TEXT, author TEXT, year INTEGER)')
curs.execute('INSERT INTO books VALUES ("The Hobbit", "J.R.R. Tolkien", 1937)')
curs.execute('INSERT INTO books VALUES ("Small Gods", "Terry Pratchett", 1992)')
curs.execute('INSERT INTO books VALUES ("Thud!", "Terry Pratchett", 2005)')
conn.commit()
conn.close()

#  Now we use SQLAlchemy to connect and perform the alphabetical select.
engine = create_engine('sqlite:///books.db')
metadata = MetaData()
# Reflect the table from the existing database
books_table = Table('books', metadata, autoload_with=engine)

# Construct the alphabetical query
query = select(books_table.c.title).order_by(books_table.c.title)

print("Result of 16.8 (Alphabetical Titles via SQLAlchemy):")
with engine.connect() as connection:
    result = connection.execute(query)
    for row in result:
        print(row[0]) 