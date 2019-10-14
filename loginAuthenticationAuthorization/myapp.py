# Flask main application

from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config.from_pyfile('config.py')
from views import *
mongo = PyMongo(app)

if __name__ == '__main__':
    app.run()