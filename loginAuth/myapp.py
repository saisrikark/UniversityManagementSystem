# Flask main application

from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config.from_pyfile('config.py')
from config import client
from loginAuthViews import loginAuthAPI

app.register_blueprint(loginAuthAPI)

if __name__ == '__main__':
    app.run(port=5000)