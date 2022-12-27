## Why use python + SQL
Since SQL is a programming language which purpose is to query data to a database, it doesn't much else. Granted depending on which database you choose, you will get more functionality, but one of the most bare bones databases, sqlite, offers pretty much only the bare necessities. 

Thus, in order to couple SQL with other applications one can use other languages, such as python, to connect the database. There are many packages that allow python to communicate with your database, one of the most popular being SQLAlchemy. It provides many functionalities such as:

* Abstract away the differences between different database engines. Thus you can write the same code for different engines (sqlite, mysql...).
* Support for object-relational mapping (ORM), which allows you to map your Python objects to database tables.
* Support for database migrations, which can make it easier to manage changes to your database schema.

## How do I use SQLAlchemy then?
Simple. You install sqlalchemy:
```bash
pip install sqlalchemy
```
Then you create an engine which you can interact with programatically in python:
```python
from sqlalchemy import create_engine
engine = create_engine('<database_URI>')
```
With this engine you can perform various SQL actions. Here we will fetch all the information from a table called employees. For more information about SQL check out the other [documentation](docs/SQL.md)
```python
employees = engine.execute('SELCECT * FROM employees')
for employee in employees:
    print(employee)
```
## How do I create tables using SQLAlchemy
This is a little more complicated question than it might seem.
We will start by using declarative_base() function. In the SQLAlchemy library, the `declarative_base()` function is used to create a base class for defining the schema of a database in an object-oriented way. Here is an example on how to use it:

```python
# We import column types which can be used when defining Table objects.
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')

#Creates an instance of declarative_base
Base = declarative_base()

#Creates as User class that inherits the Base instance
class User(Base):
    # the name of the table which we will be able to find in the databse
    __tablename__ = 'users'
    # The column names and their respective types
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

Base.metadata.create_all(engine)
```

This will create the User schema for the database. Then we can use python classes to query data using session_maker:
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

user = User(name='John', email='john@example.com')

session.add(user)
session.commit()
```
Then we can query data like this:
```python
# Fetches all of the information from the database
users = session.query(User).all()
for user in users:
    print(user)

# Filters out only users which has the name John
users = session.query(User).filter(User.name == 'John').all()
for user in users:
    print(user)
# Fetches all users and sorts them by name
users = session.query(User).order_by(User.name).all()
for user in users:
    print(user)
```

