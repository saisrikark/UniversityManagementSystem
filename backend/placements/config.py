#CONFIGURATION FILE for placement microservice
from pymongo import MongoClient

UPLOAD_FOLDER = '/home/hduser/edu-breeze/backend/placements/uploads'
MAX_CONTENT_LENGTH = 16*1024*1024
client = MongoClient("localhost:27017")
