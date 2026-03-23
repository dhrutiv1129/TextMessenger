import sqlite3
import time
import subprocess
from openai import OpenAI

DB_PATH = "/Users/dhrutivadlamudi/Library/Messages/chat.db"

def get_latest_message():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT text, is_from_me, date
        FROM message
        ORDER BY date DESC
        LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()
    return row


client = OpenAI()


def generate_reply(text):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Dhruti texting her friend casually."},
            {"role": "user", "content": text}
        ]
    )

    return completion.choices[0].message.content


def send_imessage(phone, text):
    # escape quotes so AppleScript doesn't break
    text = text.replace('"', '\\"')

    script = f'''
    tell application "Messages"
        set targetBuddy to buddy "{phone}" of service "iMessage"
        send "{text}" to targetBuddy
    end tell
    '''

    subprocess.run(["osascript", "-e", script])


last_seen = None

while True:
    msg = get_latest_message()

    if msg and msg[0] and msg[1] == 0:  # incoming message with text
        if msg[2] != last_seen:
            print("New message:", msg[0])

            response = generate_reply(msg[0])
            send_imessage("FRIEND_PHONE_NUMBER", response)

            last_seen = msg[2]

    time.sleep(5)