#CONFIGURATION FILE FOR FLASK AND MONGODB

DEBUG = True

#Add more mongoDB stuff here
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"