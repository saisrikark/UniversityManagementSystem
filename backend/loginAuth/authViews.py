from flask import jsonify, request, Blueprint

authAPI = Blueprint('authAPI',__name__)

from myapp import client

#### Auhorization part beginning ####### ##############################################
def matchPermissionLevel(role, operation):
    ret = False
    if(role == '2'): # For management they can do anything
        ret = True
    elif(role == '1'): # For teachers
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


@authAPI.route('/auth' + '/authUserOnResource', methods=['POST'])
def userAuthorizationOnResource():
    response = {}
    code = None
    operation = request.json["operation"] # C R U D
    requesterId = request.json["requesterId"]
    resourceId = request.json["resourceId"]
    resourceType = request.json["resourceType"] 
    # Will be needed when we check for difference between blog and other resources
    resourceOwnerId = request.json["resourceOwnerId"]
    token = request.json["token"]
    role = request.json["role"]
    if(not checkForResource(resourceId, resourceType)):
        code = 404
        response = {"access" : 0}
    res = request.get_data(str(token))
    if(res.json['login']):
        code = 401
        response = {"access" : 0}
    elif((requesterId == resourceOwnerId) or 
    matchPermissionLevel(role, operation)):
        code = 200
        response = {"access" : 1}
    else:
        code = 200
        response = {"access" : 0}   
    return jsonify(response), code

#  Authorization part ending ##############