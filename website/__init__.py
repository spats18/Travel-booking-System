#to make website a package
from flask import Flask

def create_app():
    app = Flask(__name__) # initialization of flask
    app.config['SECRET_KEY'] = 'random key to encrypt' # encrypt and secure the cookies and session data related to our website

    return app
    # So above will create the Flask Application and initialize the secret key and we returned it through above function

    # now import this website package and run this app created thru main.py