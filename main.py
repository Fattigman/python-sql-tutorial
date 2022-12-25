from init_db import init_db, engine


def read_db():
    # Select all users from the database from the engine
    users = engine.execute('SELECT * FROM users')
    for user in users:
        print(user)

    # Select all items from the database from the engine
    items = engine.execute('SELECT * FROM items')
    for item in items:
        print(item)


if __name__ == '__main__':
    init_db()
    # Select all users from the database from the engine
    read_db()

