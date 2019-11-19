from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "secret key"
app.config['MONGO_URI'] = "mongodb://localhost:27017/eb-user-ms" #"mongodb://localhost:27017/eb-user-ms"
CORS(app)
mongo = PyMongo(app)
