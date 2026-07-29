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

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dockerized Flask & MySQL App</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Segoe UI', Arial, sans-serif;
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #e2e8f0;
  }}
  .card {{
    background: #1e2937;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 48px 56px;
    text-align: center;
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    max-width: 480px;
  }}
  .icon {{
    font-size: 48px;
    margin-bottom: 16px;
  }}
  h1 {{
    font-size: 24px;
    margin-bottom: 12px;
    color: #f1f5f9;
  }}
  p.subtitle {{
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 32px;
  }}
  .counter {{
    background: #0f172a;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 24px;
  }}
  .counter .number {{
    font-size: 48px;
    font-weight: 700;
    color: #38bdf8;
    line-height: 1;
  }}
  .counter .label {{
    color: #94a3b8;
    font-size: 13px;
    margin-top: 8px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }}
  .stack {{
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
  }}
  .badge {{
    background: #334155;
    color: #cbd5e1;
    font-size: 12px;
    padding: 6px 12px;
    border-radius: 999px;
  }}
  footer {{
    margin-top: 28px;
    color: #64748b;
    font-size: 12px;
  }}
</style>
</head>
<body>
  <div class="card">
    <div class="icon">🐳</div>
    <h1>Dockerized Flask &amp; MySQL App</h1>
    <p class="subtitle">Running in containers, orchestrated with Docker Compose, deployed on Railway.</p>
    <div class="counter">
      <div class="number">{count}</div>
      <div class="label">Total Visits</div>
    </div>
    <div class="stack">
      <span class="badge">Flask</span>
      <span class="badge">MySQL 8.0</span>
      <span class="badge">Docker</span>
      <span class="badge">Railway</span>
    </div>
    <footer>Refresh the page to increment the counter</footer>
  </div>
</body>
</html>"""

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
    return PAGE_TEMPLATE.format(count=count)

if __name__ == "__main__":
    # Listen on all interfaces, port 5000
    app.run(host="0.0.0.0", port=5000)