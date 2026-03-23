import sqlite3

DB_PATH = "/Users/dhrutivadlamudi/Library/Messages/chat.db"

try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT text, is_from_me
        FROM message
        ORDER BY date DESC
        LIMIT 5
    """)

    rows = cursor.fetchall()
    conn.close()

    print("Recent messages:")
    for row in rows:
        print(row)

except Exception as e:
    print("Error:", e)