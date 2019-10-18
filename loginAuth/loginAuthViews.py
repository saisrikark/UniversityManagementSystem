from flask import render_template, request, jsonify, Blueprint
from hashlib import sha256
from random import randint

loginAuthAPI = Blueprint('loginAuthAPI', __name__)

from myapp import app, client

loginBase = "/login"
authBase = "/authorization"

db = client.eb
userCollection = db.user
permissionCollection = db.permission
loggedInUsersCollection = db.loggedIn
resourceCollection = db.resource

#################################### Helpers Beginning ####################################
def testDatabase():
    post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"]}
    postId = userCollection.insert_one(post).inserted_id
    print(postId)

def isEmpty(object):
    if(object is None):
        return True
    return False

'''
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Origin','127.0.0.1')
    return response
'''
######################################## Helpers Ending ###########################################

########################################### Login Part Beginning ##################################
@loginAuthAPI.route(loginBase)
def index():
    return render_template('loginPage.html')

def saveToLoggedInUser(username, token):
    loggedInUsersCollection.insert_one(
        {'userId': username, 'token' : token})

def checkPassword(dbPassword, receivedPassword):
    #hashed = sha256(dbPassword)
    hashed = dbPassword
    if(hashed == receivedPassword):
        return True
    return False

def generateToken():
    return randint(999999,100000000)
    
@loginAuthAPI.route(loginBase + '/loginSubmission', methods=['POST'])
def loginSubmission():
    code = None
    response = dict()
    username = request.json['username']
    password = request.json['password']
    mongoLoggedInUsers = loggedInUsersCollection.find_one(
        {"username" : username})
    if(isEmpty(mongoLoggedInUsers)):
        mongoResponse = userCollection.find_one({"username" : username})
        if(isEmpty(mongoResponse)):
            code = 404
        else:
            if(checkPassword(mongoResponse['password'], password)):
                code = 200
                token = generateToken()
                saveToLoggedInUser(mongoResponse["userId"], token)
                response["token"] = token
                response["userId"] = mongoResponse["userId"]
                response["userType"] = mongoResponse["userType"]
            else:
                code = 401 # Invalid credentials
    else:
        code = 405 # Already logged in
    return jsonify(response), code
########################################### Login Part Ending #####################################

########################################### Logout Part Beginning #################################
def removeFromLoggedInUsers(userId, token):
    loggedInUsersCollection.remove(
        {"userId" : userId, "token" : token})

@loginAuthAPI.route(loginBase + '/logout', methods=['POST'])
def logout():
    code = None
    response = {}
    userId = request.json["userId"]
    token = request.json["token"]
    mongoResponse = loggedInUsersCollection.find_one(
        {"userId" : userId, "token" : token})
    if(isEmpty(mongoResponse)):
        code = 404
        response = {"status" : "Not logged in"}
    else:
        code = 200
        response = {"status" : "Logged out"}
        removeFromLoggedInUsers(userId, token)      
    return jsonify(response), code
########################################### Logout Part Ending ####################################

########################################### Authorization Beginning ###############################
'''
What is the authorization on resource request ?
what kind of resource ? blog or other
operation : C R U D
resource id
token
userId of person sending the request
userType - 0 , 1, 2 (student , teacher, management)

response - can do or not
'''
def matchPermissionLevel(userType, operation):
    ret = False
    if(userType == '2'): # For management
        ret = True
    elif(userType == '1'): # For teachers
        if(operation in ['C', 'R', 'U']):
            ret = True
    else: # For students
        if(operation in ['C', 'R']):
            ret = True
    return ret

def checkForResource(resourceId, resourceType):
    #Checks if the resource is present or not
    #To be filled
    return True

@loginAuthAPI.route(authBase + '/authUserOnResource', methods=['POST'])
def userAuthorizationOnResource():
    response = {}
    code = None
    operation = request.json["operation"]
    requesterId = request.json["requesterId"]
    resourceId = request.json["resourceId"]
    resourceType = request.json["resourceType"]
    resourceOwnerId = request.json["resourceOwnerId"]
    token = request.json["token"]
    userType = request.json["userType"]
    if(not checkForResource(resourceId, resourceType)):
        code = 404
        response = {"access" : 0}
    checkUserLoggedIn = loggedInUsersCollection.find_one(
        {"userId" : requesterId, "token" : token})
    if(isEmpty(checkUserLoggedIn)):
        code = 401
        response = {"access" : 0}
    elif(requesterId == resourceOwnerId):
        code = 200
        response = {"access" : 1}
    elif(matchPermissionLevel(userType, operation)):
        code = 200
        response = {"access" : 1}
    else:
        code = 200
        response = {"access" : 0}        
    return jsonify(response), code
########################################### Authorization Ending ##################################