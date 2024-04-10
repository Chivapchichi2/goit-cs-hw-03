from faker import Faker
import psycopg2
import random
from db_connection import create_connection

fake = Faker()

def seed_users(num_users):
    conn = create_connection()
    cursor = conn.cursor()
    for _ in range(num_users):
        fullname = fake.name()
        email = fake.email()
        cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
    conn.commit()
    cursor.close()
    conn.close()

def seed_statuses():
    conn = create_connection()
    cursor = conn.cursor()
    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cursor.execute("INSERT INTO status (name) VALUES (%s)", (status,))
    conn.commit()
    cursor.close()
    conn.close()

def seed_tasks(num_tasks):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cursor.fetchall()]
    for _ in range(num_tasks):
        title = fake.sentence()
        description = fake.text()
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                       (title, description, status_id, user_id))
    conn.commit()
    cursor.close()
    conn.close()

