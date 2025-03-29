import os
import psycopg2
from psycopg2.extras import RealDictCursor
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment variables.
DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    st.error("DATABASE_URL is not set in the .env file")
    st.stop()


def connect_to_database():
    """
    Establish a connection to the PostgreSQL database.
    Returns the connection object.
    """
    try:
        conn = psycopg2.connect(DB_URL)
        return conn
    except psycopg2.Error as e:
        st.error(f"Error connecting to the database: {e}")
        st.stop()


def create_mood_table(conn):
    """
    Create the mood_log table if it does not exist.
    """
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mood_log (
                id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                mood VARCHAR(20) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
    conn.commit()


def save_mood(conn, user_name, mood):
    """
    Insert a new mood entry for the given user into the database.
    """
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO mood_log (user_name, mood)
            VALUES (%s, %s);
        """, (user_name, mood))
    conn.commit()


def load_mood_log(conn, user_name):
    """
    Retrieve all mood entries for the given user from the database.
    Returns a list of dictionaries.
    """
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("""
            SELECT id, user_name, mood, created_at
            FROM mood_log
            WHERE user_name = %s
            ORDER BY created_at DESC;
        """, (user_name,))
        return cursor.fetchall()


def load_last_mood(conn, user_name):
    """
    Retrieve the most recent mood entry for the given user.
    Returns the mood string if found; otherwise, returns None.
    """
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("""
            SELECT mood
            FROM mood_log
            WHERE user_name = %s
            ORDER BY created_at DESC
            LIMIT 1;
        """, (user_name,))
        result = cursor.fetchone()
        if result:
            return result['mood']
        return None
