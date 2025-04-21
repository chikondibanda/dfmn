import sqlite3
from models import User


def db_connect():
    """Connect to the SQLite database with a timeout."""
    conn = sqlite3.connect(
        'mentorship.db', timeout=10)  # Set a timeout to avoid "database is locked" errors
    # Enable Write-Ahead Logging for better concurrency
    conn.execute('PRAGMA journal_mode=WAL;')
    return conn


def init_db():
    """Initialize the database with tables."""
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            location TEXT,
            role TEXT NOT NULL CHECK (role IN ('mentor', 'mentee', 'admin')),
            profile_picture TEXT,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER,
            user_id INTEGER,
            content TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (topic_id) REFERENCES topics (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER,
            receiver_id INTEGER,
            content TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (sender_id) REFERENCES users (id),
            FOREIGN KEY (receiver_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()


def create_user(conn, user):
    """
    Create a new user.

    :param conn: Connection object.
    :param user: User object.
    """
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (firstname, lastname, username, email, phone, location, role, password)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user.firstname, user.lastname, user.username, user.email, user.phone, user.location, user.role, user.password))
    conn.commit()


def get_user(conn, user_id):
    """
    Query user by ID.

    :param conn: Connection object.
    :param user_id: ID of the user to query.
    :return: User object.
    """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    row = cursor.fetchone()
    if row:
        return User(*row)
    else:
        return None


# Initialize the database
init_db()
