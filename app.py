from flask import Flask
import os, time
import mysql.connector

app = Flask(__name__)

def get_db():
    # Simple retry so first request works even if DB is still warming up
    retries = 10
    while retries:
        try:
            return mysql.connector.connect(
                host=os.environ['DB_HOST'],
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASSWORD'],
                database=os.environ['DB_NAME']
            )
        except Exception as e:
            retries -= 1
            time.sleep(2)
    # Final attempt (let it raise for visibility)
    return mysql.connector.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME']
    )

@app.route("/")
def home():
    db = get_db()
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255))")
    cur.execute("INSERT INTO visits (message) VALUES ('Hello from Flask!')")
    db.commit()
    cur.execute("SELECT COUNT(*) FROM visits")
    count = cur.fetchone()[0]
    cur.close()
    db.close()
    return f"Hello! This page has been visited {count} times.\n"

if __name__ == "__main__":
    # Listen on all interfaces, port 5000
    app.run(host="0.0.0.0", port=5000)
