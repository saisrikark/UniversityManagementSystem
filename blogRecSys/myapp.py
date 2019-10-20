# Flask main application

from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config.from_pyfile('config.py')
from config import client
from blogRecSysViews import blogRecSysAPI

app.register_blueprint(blogRecSysAPI)

if __name__ == '__main__':
    app.run(port=5000)