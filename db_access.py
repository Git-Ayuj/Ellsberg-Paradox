import psycopg2
import os

class Database:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(database="deh1869hc6qg19", user="vgtdraajfeajld", password="cbae9e0a9b0691a1e14838758de0b86ad516a3318f1ecfca28da10941530bfbd", host="ec2-52-204-72-14.compute-1.amazonaws.com", port="5432")
        except Exception as e:
            print(e)
        self.cursor = self.connection.cursor()

        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS desc_demo
                (session_id SERIAL PRIMARY KEY,
                 time_stamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                 age INT,
                 gender VARCHAR(10),
                 education VARCHAR(50),
                 major VARCHAR(100),
                 occupation VARCHAR(100),
                 marital_status VARCHAR(100),
                 income VARCHAR(100))''')
            print("created desc_demo.")
        except Exception as e:
            print("desc_demo not created.")
            print(e)

        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS exp_demo
                (session_id SERIAL PRIMARY KEY,
                 time_stamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                 age INT,
                 gender VARCHAR(10),
                 education VARCHAR(50),
                 major VARCHAR(100),
                 occupation VARCHAR(100),
                 marital_status VARCHAR(100),
                 income VARCHAR(100))''')
            print("created exp_demo.")
        except Exception as e:
            print("exp_demo not created.")
            print(e)

        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS desc_outcomes
                (session_id INTEGER,
                 time_stamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                 proportion_a INT,
                 preference char(1),
                 people_saved INT,
                 FOREIGN KEY (session_id) REFERENCES desc_demo(session_id))''')
            print("created desc_outcomes.")
        except Exception as e:
            print("desc_outcomes not created.")
            print(e)

        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS exp_outcomes
                (session_id INTEGER,
                 time_stamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                 proportion_a INT,
                 preference char(1),
                 people_saved INT,
                 FOREIGN KEY (session_id) REFERENCES exp_demo(session_id))''')
            print("created exp_outcomes.")
        except Exception as e:
            print("exp_outcomes not created.")
            print(e)

        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS exp_sampling
                (session_id INT,
                 time_stamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                 program char(1),
                 people_saved INT,
                 PRIMARY KEY (session_id, time_stamp),
                 FOREIGN KEY (session_id) REFERENCES exp_demo(session_id))''')
            print("created exp_sampling.")
        except Exception as e:
            print("exp_sampling not created.")
            print(e)

        self.getSessionId()
    
    def execute(self, query):
        self.cursor.execute(query)
        return list(self.cursor.fetchall())

    def insertDemo(self, record, table_name):
        self.cursor.execute(f"INSERT INTO {table_name} (age, gender, education, major, occupation, marital_status, income) VALUES {record}")
        self.connection.commit()

    def insertOutcomes(self, record, table_name):
        self.cursor.execute(f"INSERT INTO {table_name} (session_id, proportion_a, preference, people_saved) VALUES {record}")
        self.connection.commit()
        self.getSessionId()

    def insertSample(self, record):
        self.cursor.execute(f"INSERT INTO exp_sampling (session_id, program, people_saved) VALUES {record}")
        self.connection.commit()

    def getSessionId(self):
        exp = self.execute('SELECT COALESCE(MAX(session_id), 0) FROM exp_demo')[0][0]
        desc = self.execute('SELECT COALESCE(MAX(session_id), 0) FROM desc_demo')[0][0]
        self.exp_sid, self.desc_sid = exp + 1, desc + 1

    def show(self):
        tables = self.execute("""SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
        AND table_type='BASE TABLE'""")

        for table in tables:
            print("\n============")
            print(table[0])
            rows = self.execute(f"SELECT * from {table[0]}")
            for row in rows:
                print(row)
            print("============\n")

    def __del__(self):
        self.connection.close()

db = Database()