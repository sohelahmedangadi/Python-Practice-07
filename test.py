import psycopg2
def table():
    # Connecting to PSQL using python
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="@Sohail1",host="localhost",port="5432")

    # Creating table using python
    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')
    print("Table Created Successfully")

    conn.commit()
    conn.close()

# table()

def data():
    # Connecting to PSQL using python
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="@Sohail1",host="localhost",port="5432")

    # Inserting data in table using python
    cursor = conn.cursor()
    cursor.execute('''insert into employees(Name,ID,AGE) values('Sunil',01,21);''')
    print("Data Added Successfully")

    conn.commit()
    conn.close()

# data()

def extract():
    # Connecting to PSQL using python
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="@Sohail1",host="localhost",port="5432")

    # Extracting data from table using python
    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    show = cursor.fetchone()
    print(show[0:3])
    # print("Data Added Successfully")

    conn.commit()
    conn.close()

extract()

def data():
    # Connecting to PSQL using python
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="@Sohail1",host="localhost",port="5432")

    # Inserting data in table using python
    cursor = conn.cursor()

    name = input("Enter a name: ")
    id = input("Enter id: ")
    age = input("Enter age: ")

    query = '''insert into employees(Name,ID,AGE) values(%s,%s,%s);'''
    cursor.execute(query,(name,id,age))

    print("Data Added Successfully")

    conn.commit()
    conn.close()

# data()






