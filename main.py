from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
# to create a provide front end UI to the user
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin123@localhost:8080/tourism_db'
app.config['SECRET_KEY'] = 'd0063c4e0a1b18016d982395e18ea5ca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CACHE_TYPE'] = 'SimpleCache'
db = SQLAlchemy(app)

login_manager = LoginManager(app)

from routes import *
if __name__ == '__main__':
    app.run(debug=True, port=1235, threaded=True, host="localhost")