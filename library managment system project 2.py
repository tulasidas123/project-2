import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Tables
cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, name TEXT, author TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS members(id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS issue(book_id INTEGER, member_id INTEGER)")

conn.commit()

def add_book():
    name = input("Book name: ")
    author = input("Author: ")
    cursor.execute("INSERT INTO books(name, author) VALUES (?,?)", (name, author))
    conn.commit()

def add_member():
    name = input("Member name: ")
    cursor.execute("INSERT INTO members(name) VALUES (?)", (name,))
    conn.commit()

def issue_book():
    b = int(input("Book ID: "))
    m = int(input("Member ID: "))
    cursor.execute("INSERT INTO issue VALUES (?,?)", (b, m))
    conn.commit()

def view_books():
    for row in cursor.execute("SELECT * FROM books"):
        print(row)

while True:
    print("\n1.Add Book 2.Add Member 3.Issue 4.View 5.Exit")
    ch = input("Choice: ")
    if ch=="1": add_book()
    elif ch=="2": add_member()
    elif ch=="3": issue_book()
    elif ch=="4": view_books()
    else: break

conn.close()
