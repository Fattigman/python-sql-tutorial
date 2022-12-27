# What is alembic?
Alembic is a database migration tool. 

Ok, what is a database migration tool?

Imagine you have a database that you want to update, that might include creating new tables, updating/deleting old ones. Manually this would take a long time with a lot of SQL statements. Thankfully with alembic we don't have to do it manually! As long as we stick to our sqlalchemy Base classes we can generate this migration scripts automatically using alembic. Kind of like git for databases (but not entirely).

## Initiating alembic

Start by install alembic with pip

```bash
pip install alembic
```

We then have a database schema like so:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
```

In the same folder run:
```bash
alembic init alembic
```
This will create an alimbic folder with all the configuration for the project. In the `alembic.ini` file, edit the sqlalchemy url to the url you use in the project
```conf
sqlalchemy.url = sqlite:///database.db
```
Then you can generate the migration scripts using following command:
```bash
alembic revision -m "Create users table"
```
This will generate the necessary migration scripts which can be applied by running:
```bash
alembic upgrade head
```

## Updating alembic version

Now we want to update the user model, say we want an age field as well:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
```
Then run `alembic revision`:
```shell
alembic revision -m "Add age field to users table"
```
Then we can upgrade the database by running:
```
alembic upgrade head
```
And if you regret your decision you can always do a rollback:
```
alembic downgrade -1
```