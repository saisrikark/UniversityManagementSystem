#CONFIGURATION FILE FOR FLASK AND MONGODB

from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient

DEBUG = True

#MongoDB Config
URI = 'mongodb+srv://srikar:srikar@cluster0-zhltr.mongodb.net/test?retryWrites=true&w=majority'
client = MongoClient(URI)

secret_key = "secret key"
MONGO_URI = URI #"mongodb://localhost:27017/eb-user-ms"