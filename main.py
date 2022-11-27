from flask import Flask
from routes import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
# to create a provide front end UI to the user
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin123@localhost:8080/tourism_db'
app.config['SECRET_KEY'] = 'd0063c4e0a1b18016d982395e18ea5ca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

login_manager = LoginManager(app)

if __name__ == '__main__':
    app.run(debug=True, port=1234, threaded=True)
