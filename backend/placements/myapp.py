from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config.from_pyfile('config.py')
from config import client
from placementViews import placementAPI
from endorsementViews import endorsementAPI

app.register_blueprint(placementAPI)
app.register_blueprint(endorsementAPI)

if __name__ == '__main__':
	app.run('0.0.0.0', port = 5002)
