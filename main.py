from create_tables import create_tables
from seed import seed_users, seed_statuses, seed_tasks

def main():
    # Create tables
    create_tables()

    # Sead Fake data
    seed_users(10)  # generate 10 users
    seed_statuses() # generate statuses
    seed_tasks(20)  # generate 20 tasks

if __name__ == "__main__":
    main()
