import sqlite3 as sq
from sqlite3 import Cursor

# Connect DB
conn = sq.connect('database.db')
cursor = conn.cursor()

# Create the table if not exists
cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT
                    )
                """)

conn.commit()


# Create Register - (C)
def create_user(name: str, email) -> str:
    cursor.execute('INSERT INTO users (name, email) VALUES(?, ?)', (name, email))
    conn.commit()
    return "User added"


# Load Registers
def load_registers() -> list:
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    list_users = []
    for user in users:
        list_users.append(user)
    return list_users


# Read User by id - (R)
def read_user(id: int):
    cursor.execute('SELECT id, name, email FROM users WHERE id = ?', (id,))
    user = cursor.fetchall()

    if user:
        return user
    else:
        return "User not founded"


# Update User - (U)
def update_user(id: int, name: str, email: str) -> str:
    cursor.execute('UPDATE users SET name=?, email=? WHERE id=?', (name, email, id))
    conn.commit()
    return "User updated"


# Delete User - (D)
def delete_user(id: int) -> str:
    cursor.execute('DELETE FROM user WHERE id=?', (id,))
    conn.commit()
    return "User deleted"