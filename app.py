# app.py

from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__) # application 'app' is object of class 'Flask'
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'MySQL123/'
app.config['MYSQL_DATABASE_DB'] = 'test_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

# To use MySQL, we need a cursor:
    # Creating a connection cursor

conn = mysql.connect()
cursor = conn.cursor()

# To create a table:
table_name = "test" # <--- Change table name
table_definition = "(Id INT AUTO_INCREMENT PRIMARY KEY, Question VARCHAR(255), Answer VARCHAR(255))"
table_columns = f"(Question, Answer)"
table_values = f"('What is your name?', 'John')"

print(f"CREATE TABLE IF NOT EXISTS {table_name} {table_definition}")
cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} {table_definition}")
cursor.execute(f"INSERT INTO {table_name} {table_columns} VALUES {table_values}")

#Closing the cursor
cursor.close()
conn.close()

# import routes
from routes import *


if __name__ == '__main__':
    # '0.0.0.0' = 127.0.0.1 i.e. localhost
    # port = 5000 : we can modify it for localhost
    app.run(host='0.0.0.0', port=5010, debug=True) # local webserver : app.run()