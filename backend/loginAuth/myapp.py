# Flask main application
from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config.from_pyfile('config.py')

from config import secret_key, MONGO_URI, client
mongo = PyMongo(app)

from loginViews import loginAPI
from authViews import authAPI

app.register_blueprint(loginAPI)
app.register_blueprint(authAPI)

if(__name__ == '__main__'):
    app.run(port=3000)
