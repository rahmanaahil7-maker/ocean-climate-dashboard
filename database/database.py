import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = 'database/ocean_data.db'

class User(UserMixin):
    def __init__(self, id, email, password_hash):
        self.id = id
        self.email = email
        self.password_hash = password_hash

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create observations table if missing
    cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='observations'")
    if cursor.fetchone()[0] == 0:
        end_date = datetime.now()
        dates = pd.date_range(end=end_date, periods=90, freq='D')
        df = pd.DataFrame({
            'Date': dates.strftime('%Y-%m-%d'),
            'Temp_C': np.round(np.random.normal(loc=16.5, scale=1.5, size=90), 2),
            'Wave_Height_m': np.round(np.random.uniform(1.0, 5.5, size=90), 2),
            'Wind_Speed_kmh': np.round(np.random.uniform(10.0, 50.0, size=90), 2)
        })
        df.to_sql('observations', conn, index=False)
    # Create user alert settings table if missing
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_settings (
            user_id INTEGER PRIMARY KEY,
            temp_threshold FLOAT DEFAULT 28.0,
            alerts_enabled BOOLEAN DEFAULT 1,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')    
    # Create users table if missing
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, password_hash FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(id=row[0], email=row[1], password_hash=row[2])
    return None

def get_user_by_id(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, password_hash FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(id=row[0], email=row[1], password_hash=row[2])
    return None

def create_user(email, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    try:
        cursor.execute("INSERT INTO users (email, password_hash) VALUES (?, ?)", (email, hashed_password))
        conn.commit()
        success = True
    except sqlite3.IntegrityError:
        success = False
    conn.close()
    return success

def get_filtered_data(start_date, end_date):
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM observations"
    conditions = []
    if start_date:
        conditions.append(f"Date >= '{start_date}'")
    if end_date:
        conditions.append(f"Date <= '{end_date}'")
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY Date ASC"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_user_settings(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT temp_threshold, alerts_enabled FROM user_settings WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"temp_threshold": row[0], "alerts_enabled": bool(row[1])}
    return {"temp_threshold": 28.0, "alerts_enabled": True}

def update_user_settings(user_id, temp_threshold, alerts_enabled):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_settings (user_id, temp_threshold, alerts_enabled)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            temp_threshold = excluded.temp_threshold,
            alerts_enabled = excluded.alerts_enabled
    ''', (user_id, temp_threshold, int(alerts_enabled)))
    conn.commit()
    conn.close()