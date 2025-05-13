from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        database=os.getenv("POSTGRES_DB", "flaskdb"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "password"),
        host="postgres",  # Service name in Kubernetes
        port="5432"
    )
    return conn

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        conn.close()
        return "Connected to PostgreSQL!", 200
    except Exception as e:
        return f"Database connection error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
