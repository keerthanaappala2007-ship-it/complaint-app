import sqlite3

conn = sqlite3.connect("complaints.db", check_same_thread=False)
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            room TEXT,
            complaint TEXT,
            category TEXT,
            status TEXT
        )
    """)
    conn.commit()

def add_complaint(name, room, complaint, category):
    cursor.execute("""
        INSERT INTO complaints (name, room, complaint, category, status)
        VALUES (?, ?, ?, ?, ?)
    """, (name, room, complaint, category, "Pending"))
    conn.commit()

def get_all_complaints():
    cursor.execute("SELECT * FROM complaints")
    return cursor.fetchall()

def update_status(id, status):
    cursor.execute("UPDATE complaints SET status=? WHERE id=?", (status, id))
    conn.commit()