# Flask main application

from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config.from_pyfile('config.py')
from config import client
from fileViews import filesAPI

app.register_blueprint(filesAPI)

if __name__ == '__main__':
    app.run('127.0.0.1', port=5006)
