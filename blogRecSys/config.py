#CONFIGURATION FILE FOR FLASK AND MONGODB

from pymongo import MongoClient

DEBUG = True

#MongoDB Config

client = MongoClient('mongodb+srv://srikar:srikar@cluster0-zhltr.mongodb.net/test?retryWrites=true&w=majority')