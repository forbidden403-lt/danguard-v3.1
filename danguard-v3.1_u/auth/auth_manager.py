import os
import sqlite3
import bcrypt
from config import Config

def setup_db():
    """Membuat tabel user dan folder database jika belum ada."""
    os.makedirs('database', exist_ok=True)
    conn = sqlite3.connect(Config.DATABASE_URL.replace('sqlite:///', ''))
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            telegram_chat_id TEXT
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password, telegram_chat_id):
    """Mendaftarkan user baru. Hanya untuk admin."""
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        conn = sqlite3.connect(Config.DATABASE_URL.replace('sqlite:///', ''))
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password_hash, telegram_chat_id) VALUES (?, ?, ?)",
                       (username, password_hash, telegram_chat_id))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    """Memverifikasi login user."""
    conn = sqlite3.connect(Config.DATABASE_URL.replace('sqlite:///', ''))
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, telegram_chat_id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        return True, result[1]
    return False, None