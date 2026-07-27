import sqlite3

DATABASE = "appointments.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        reason TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()