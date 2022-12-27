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

## How do I create data in SQL
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

And then we can get the information by doing following:
```sql
-- Will get all information
SELECT * FROM employees;
-- Will only get the id and name columns
SELECT id, name FROM employees;
-- Will only show entries with a hire_date later than 2022-01-01
SELECT * FROM employees WHERE hire_date > '2022-01-01';
```
## SQL is a relational database
SQL is also a so called relational database, meaning you can link tables to each other via keys, creating so called relations between the data. In the following case, we will create a table that is linked to the employees table via a key:

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

Then we can query data from several tables and filter based on only what we are looking for:

```sql
SELECT e.id, e.name, e.hire_date, p.name AS project_name
FROM employees e
JOIN projects p ON e.id = p.employee_id
WHERE e.name = 'Jane Doe';
```

This `SELECT` statement uses a `JOIN` clause to combine data from the "employees" and "projects" tables based on a shared key (the employee's ID). The `ON` clause specifies the join condition, which is that the "id" column from the "employees" table must be equal to the "employee_id" column from the "projects" table.

The `AS` clause is used to give the "name" column from the "projects" table an alias of "project_name," which makes it easier to distinguish between the two "name" columns in the resulting data set.

The `WHERE` clause is used to filter the rows that are returned based on the employee's name. In this case, only rows for "Jane Doe" will be returned.

## What's a schema?
In a database management system, a schema is the organization or structure of the database. It defines the tables, fields, and relationships between them.

In SQL it translates to what tables exists in a database and what columns do these tables consist of. The schema of the examples we defined above is:
* employees
  * id
  * name
  * hire_date
* projects
  * id
  * name
  * employee_id

You can get this information by query to the database, however the command is specific to what kind of Database engine (sqlite or mysql...)