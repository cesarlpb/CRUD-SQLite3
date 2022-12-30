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

# import routes
from routes import *

if __name__ == '__main__':
    # '0.0.0.0' = 127.0.0.1 i.e. localhost
    # port = 5000 : we can modify it for localhost
    app.run(host='0.0.0.0', port=5020, debug=True) # local webserver : app.run()