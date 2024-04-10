import psycopg2
from psycopg2 import Error
from db_connection import create_connection

def create_tables():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    fullname VARCHAR(100),
                    email VARCHAR(100) UNIQUE
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS status (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) UNIQUE
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(100),
                    description TEXT,
                    status_id INTEGER,
                    user_id INTEGER,
                    FOREIGN KEY (status_id) REFERENCES status(id),
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                );
            """)
            connection.commit()
            print("Tables created successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()
            connection.close()
            print("Connection closed")
