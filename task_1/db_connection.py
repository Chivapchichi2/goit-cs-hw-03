import psycopg2
from psycopg2 import Error


def create_connection():
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="qwerty",
            host="localhost",
            port="5432"
        )
        print("Connected to the database")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
