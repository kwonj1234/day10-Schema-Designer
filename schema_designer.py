import sqlite3

def schema(dbpath = "schema_designer.db"):
    with sqlite3.connect(dbpath) as connection:
        c = connection.cursor()

        #drop tables if they exist
        dropsql = "DROP TABLE IF EXISTS {};"

        for table in ["snacks", "students", "teachers", "classes", "class1"]:
            c.execute(dropsql.format(table))

        #snacks table
        c.execute("""CREATE TABLE snacks (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    brand VARCHAR,
                    type VARCHAR,
                    price FLOAT,
                    available_quantity INTEGER
                    );""")
        
        #students and teachers table
        c.execute("""CREATE TABLE students (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR
                    );""")
        
        c.execute("""CREATE TABLE teachers (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR
                    );""")

        c.execute("""CREATE TABLE classes (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    class_num INTEGER,
                    teachers_pk INTEGER,
                    FOREIGN KEY(teachers_pk) REFERENCES teachers(pk)
                    );""")
            
        c.execute("""CREATE TABLE class1 (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_pk INTEGER,
                    classes_pk INTEGER,
                    FOREIGN KEY(student_pk) REFERENCES students(pk),
                    FOREIGN KEY(classes_pk) REFERENCES classes(pk),
                    );""")

        #employees table
        c.execute("""CREATE TABLE employees (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    ssn VARCHAR(11),
                    salary VARCHAR,
                    phone_number VARCHAR(12)
                    );""")
        
        c.execute("""CREATE TABLE departments (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR,
                    budget FLOAT
                    );""")
        
        c.execute("""CREATE TABLE department1 (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    departments_pk INTEGER,
                    employees_pk INTEGER
                    FOREIGN KEY(departments_pk) REFERENCES departments(pk)
                    FOREIGN KEY(employees_pk) REFERENCES employees(pk)
                    );""")

        #subreddit
        c.execute("""CREATE TABLE reddit_users (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR
                    );""")
                    
        c.execute("""CREATE TABLE menu (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    subscribe BOOL,
                    submit_a_post VARCHAR,
                    submit_a_comment VARCHAR
                    upvote_or_downvote BOOL
                    );""")

        c.execute("""CREATE TABLE subreddit_member (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    reddit_users_pk INTEGER,
                    FOREIGN KEY(reddit_users_pk) REFERENCES reddit_users(pk)
                    );""")

        c.execute("""CREATE TABLE subreddit_posts (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    post VARCHAR,
                    subreddit_member_pk INTEGER,
                    votes INTEGER,
                    comments VARCHAR,
                    FOREIGN KEY (subreddit_member_pk) REFERENCES subreddit_member(pk)
                    );""")

        #Art Gallery
        c.execute("""CREATE TABLE artist (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR,
                    birthplace VARCHAR,
                    age INTEGER,
                    style VARCHAR
                    );""")

        c.execute("""CREATE TABLE artwork (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR,
                    artist_pk INTEGER,
                    year_made INTEGER,
                    type VARCHAR,
                    price FLOAT,
                    FOREIGN KEY (artisit_pk) REFERENCES artist(pk)
                    );""")

        c.execute("""CREATE TABLE works by picasso (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    artwork_pk INTEGER
                    FOREIGN KEY (artwork_pk) REFERENCES artwork(pk)
                    );""")
        
        
