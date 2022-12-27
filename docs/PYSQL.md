## Why use python + SQL
Since SQL is a programming language which purpose is to query data to a database, it doesn't much else. Granted depending on which database you choose, you will get more functionality, but one of the most bare bones databases, sqlite, offers pretty much only the bare necessities. 

Thus, in order to couple SQL with other applications one can use other languages, such as python, to connect the database. There are many packages that allow python to communicate with your database, one of the most popular being SQLAlchemy. It provides many functionalities such as:

* Abstract away the differences between different database engines. Thus you can write the same code for different engines (sqlite, mysql...).
* Support for object-relational mapping (ORM), which allows you to map your Python objects to database tables.
* Support for database migrations, which can make it easier to manage changes to your database schema.

