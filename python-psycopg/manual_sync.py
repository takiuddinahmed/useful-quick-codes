import faker
import psycopg2
from faker import Faker

import config


url = config.DB_URI

def create_demo_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS demo (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )""")

def create_sync_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS sync (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )""")

def insert_demo_data(cursor):
    fake = Faker()
    for _ in range(10):
        name = fake.name()
        email = fake.email()
        cursor.execute("INSERT INTO demo (name, email) VALUES (%s, %s)", (name, email))


def setup():
    with psycopg2.connect(url) as conn:
        with conn.cursor() as cur:
            create_demo_table(cur)
            insert_demo_data(cur)
            conn.commit()

def change_data():
    with psycopg2.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM demo")
            users = cur.fetchall()
            fake = Faker()
            for user in users:
                cur.execute("UPDATE demo SET name = %s WHERE id = %s", [fake.name(), user[0]])
            conn.commit()

def sync():
    with psycopg2.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM demo")
            users = cur.fetchall()
            create_sync_table(cur)
            for user in users:

                # check if the user is in the sync table
                cur.execute("SELECT * FROM sync WHERE id = %s", (user[0],))
                sync_user = cur.fetchone()
                if not sync_user:
                    print(f"New User - {user[1]}")
                    cur.execute("INSERT INTO sync (id, name, email) VALUES (%s, %s, %s)", (user[0], user[1], user[2]))
                else:
                    if user[1] != sync_user[1] and user[2] != sync_user[2]:
                        print(f"Update User name and email - {user[1]} ")
                        cur.execute("UPDATE sync SET name = %s, email = %s WHERE id = %s", (user[1], user[2], user[0]))
                    elif user[1] != sync_user[1]:
                        print(f"Update User name - {user[1]} ")
                        cur.execute("UPDATE sync SET name = %s WHERE id = %s", (user[1], user[0]))
                    elif user[2] != sync_user[2]:
                        print(f"Update User email - {user[2]} ")
                        cur.execute("UPDATE sync SET email = %s WHERE id = %s", (user[2], user[0]))
                    else:
                        print(f"No changes - {user[1]} ")
            

            conn.commit()

        


if __name__ == "__main__":
    # setup()
    # change_data()
    sync()

