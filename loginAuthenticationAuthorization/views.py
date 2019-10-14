from myapp import app
from myapp import mongo
from models import *
from flask import render_template, request  
from flask_pymongo import PyMongo

BASE = "/login"

def updateLoggedInUsers():
    pass

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Origin','127.0.0.1')
    return response

@app.route(BASE)
def index():
    return render_template('loginPage.html')

@app.route(BASE+'loginSubmission', methods=['POST'])
def loginSubmission():
    error = None
    username = request.form["username"]
    password = request.form["password"]
    if(request.method == 'POST'):
        user = mongo.db.student.find({"username" : username})
        if(user.password == password):
            pass
    else:
        error = True
    return {"true", error}
