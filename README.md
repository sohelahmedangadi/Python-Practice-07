# Python PostgreSQL CRUD Operations

## Overview

This project demonstrates how to connect Python with a PostgreSQL database using the `psycopg2` library. It includes examples of creating a table, inserting data, and retrieving data from the database.

## Features

* Connect to a PostgreSQL database
* Create an `employees` table
* Insert employee records
* Insert user-provided data using parameterized queries
* Retrieve and display employee records

## Technologies Used

* Python 3.x
* PostgreSQL
* psycopg2

## Project Structure

```text
.
├── test.py
├── PostgreSQL Python Assignment.pdf
└── README.md
```

## Prerequisites

Before running the project, make sure you have:

* Python 3 installed
* PostgreSQL installed and running
* `psycopg2` package installed

Install the required package:

```bash
pip install psycopg2
```

## Database Configuration

Update the connection details in the Python file if needed:

```python
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="YOUR_PASSWORD",
    host="localhost",
    port="5432"
)
```

## Functions

### `table()`

Creates the `employees` table.

### `data()`

Inserts a predefined employee record into the database.

### `extract()`

Fetches and displays the first employee record from the table.

### `data()` (User Input Version)

Accepts employee details from the user and inserts them into the database using parameterized queries.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/sohelahmedangadi/Python-Practice-07.git
```

2. Move into the project directory:

```bash
cd Python-Practice-07
```

3. Install dependencies:

```bash
pip install psycopg2
```

4. Run the Python program:

```bash
python test.py
```

## Sample Output

```text
Table Created Successfully
Data Added Successfully
('Sunil', 1, 21)
```

## Learning Outcomes

* Connecting Python to PostgreSQL
* Executing SQL statements from Python
* Using parameterized SQL queries
* Reading data from a database
* Managing database transactions using `commit()`

## Author

**Sohail Ahmed**

GitHub: https://github.com/sohelahmedangadi
