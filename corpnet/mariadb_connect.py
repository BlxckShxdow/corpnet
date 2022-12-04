# Module Imports
import mariadb
import sys
import time

# Connect to MariaDB Platform
def send(data):
    try:
        conn = mariadb.connect(
            user="root",
            password="my-secret-pw",
            host="172.17.0.2",
            port=3306,
            database="mailing"
        )
        print("success")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()

    #insert information
    try:
        cur.execute("INSERT INTO mails (timestamp,mail) VALUES (?, ?)", (time.time(),data))
    except mariadb.Error as e:
        print(f"Error: {e}")

    conn.commit()
    print(f"Last Inserted ID: {cur.lastrowid}")

    conn.close()
