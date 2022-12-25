# Python + SQLAlchemy primer
This is meant as an easy primer to how to write databases with python and sqlalchemy.

This is meant as a tutorial for my colleagues

Start reading at main.py and work your way up the spider web.

## What is SQL? 
Structured Query Language, or as it is more commonly called, SQL is a standardized programming language meant to handle databases. Many types of these SQL databses, such as:
* MySQL
* Postgresql
* SQLite

A database consist of so called "Tables", which in itself consists of columns. These tables are then filled with items which are defined by what columns are specified for each table.

Columns have specific data types, most commonly:
* Integer
* Strings
* Booleans

But more abstract types exists as well. Here is an example to create on how to create a table in sql:
```sql
CREATE TABLE employees (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  hire_date DATE
);
``` 
Then you can populate this table like this:

```sql
INSERT INTO employees (id, name, hire_date)
VALUES (1, 'John Smith', '2022-01-01'),
       (2, 'Jane Doe', '2022-03-15'),
       (3, 'Bob Johnson', '2022-05-01');
```
## SQL is a relational database
SQL is also a so called relational database, meaning you can link tables to each other via keys. In the following case, we will create a table that is linked to the employees table via a key:

```sql
CREATE TABLE projects (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  employee_id INTEGER,
  FOREIGN KEY (employee_id) REFERENCES employees(id)
);
``` 
Then we populate it followingly:
```sql
INSERT INTO projects (id, name, employee_id)
VALUES (1, 'Project A', 1),
       (2, 'Project B', 2),
       (3, 'Project C', 3);
```