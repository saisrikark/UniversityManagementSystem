from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
import datetime

loginAPI = Blueprint('loginAPI',__name__)

from myapp import mongo

def createStudent(request, id):
    _id = str(id)
    _name = request.json['name']
    _semester = request.json['semester']
    _section = request.json['section']
    mongo.db.student_table.insert(
        {"studentId" : id, 'studentName': _name, 
        "semester" : _semester, "section" : _section
        })

def createTeacher(request, id):
    _id = str(id)
    _name = request.json['name']
    mongo.db.teacher_table.insert({
        'teacher_id':_id,'t_name':_name
    })

@loginAPI.route('/users/add', methods=['POST']) 
def addUser():
    # print(request.json)
    _json = request.json
    _name = _json["name"]
    _username = _json['username']
    _dateOfJoining = _json['dateOfJoining']
    _password = _json['password']
    _role = _json['role']
    _info = _json['info']

    everythingAvailable = _name and _username and _password

    if(everythingAvailable):
        # Hashed the password
        _hashedPassword = hashlib.sha256(_password['plainT'].encode())
        # construct the collection
        userCollection = {
            'name': _name,
            'username': _username,
            'dateOfJoining': _dateOfJoining,
            'password': {
                'sha256': _hashedPassword.hexdigest(),
                'lastChanged': _password['lastChanged']
            },
            'role': _role,
            'info': _info
        }

        # Checking if user exists
        numberOfusers = mongo.db.users.find({"username": _username}).count()
        if(numberOfusers != 0):
            # Username exists
            resp = jsonify({'message': 'usrExists',})
            resp.status_code = 409
            return resp

        # save in mongo
        id = mongo.db.users.insert(userCollection)
        resp = jsonify({'_id': str(id)})
        resp.status_code = 200
        if(_role == '0'):
            createStudent(request, id)
        elif(_role == '1'):
            createTeacher(request, id)
        return resp

    else:
        # Return that usr error
        resp = jsonify({'addusr': 'error'})
        resp.status_code = 500
        return resp
 
@loginAPI.route('/users/username_exists', methods=['GET'])
def checkIfUserExists():
    usernameToCheck = request.args.get('uname')
    user = mongo.db.users.find_one({ 'username': usernameToCheck})

    print(user)

    if(user):
        resp = jsonify({ 'message':'usrExists'})
        resp.status_code = 409
        return resp
        
    else:
        resp = jsonify({'message': 'noUser'})
        resp.status_code = 200
        return resp

@loginAPI.route('/users/getAll', methods=['GET'])
def getAll():
    users = mongo.db.users.find()

    userWOSecDeets = []

    for user in users:
        nuser = user
        del nuser['password']
        nuser['_id'] = str(user['_id'])
        userWOSecDeets.append(nuser) 

    resp = jsonify(userWOSecDeets)
    return resp

@loginAPI.route('/users/getUserByToken', methods=['GET'])
def getByToken():
    _token = request.args.get('token')
    tokenEntry = mongo.db.loggdInTokens.find_one({'_id': ObjectId(_token)})

    print(tokenEntry)

    if(tokenEntry):
        _userId = ObjectId(tokenEntry['userId'])
        user = mongo.db.users.find_one({'_id': _userId})

        if(user):
            del user['password']
            user['_id'] = str(user['_id'])
            resp = jsonify(user)
            resp.status_code = 404
            return resp

    resp = jsonify()
    resp.status_code = 404
    return resp

@loginAPI.route('/login', methods=['POST'])
def login():
    _json = request.json
    _username = _json['username']
    _passwordHash = _json['password']

    user = mongo.db.users.find_one({'username': _username})

    if(user):
        if(user['password']['sha256'] == _passwordHash):
            # correct password
            # create logged in user token
            tokenEntry = {
                'username': _username,
                'userId': str(user['_id']),
                'issueTimestamp': datetime.datetime.utcnow().isoformat()
            }

            print(tokenEntry)

            token = mongo.db.loggdInTokens.insert(tokenEntry)

            resp = jsonify({
                'login':True, 
                'token': str(token)
                })
            
            resp.status_code = 201
            return resp
    
    resp = jsonify({
        'login': False,
        'message': 'Wrong username or password'
    })

    resp.status_code = 403
    return resp
    
@loginAPI.route('/logout', methods=['DELETE'])
def logout():
    _token = request.args.get('token')
    print(_token)
    mongo.db.loggdInTokens.remove({'_id': ObjectId(_token)})

    resp = jsonify({'logout': True})
    resp.status_code = 202
    return resp

@loginAPI.route('/token/isLoggedIn', methods=['GET'])
def isLoggedIn():
    _token = request.args.get('token')
    tokenEntry = mongo.db.loggdInTokens.find_one({'_id': _token})

    if(tokenEntry):
        resp = jsonify({
            'login': True
        })
        resp.status_code = 200
    else:
        resp = jsonify({
            'login': False
        })
        resp.status_code = 403
    
    return resp
