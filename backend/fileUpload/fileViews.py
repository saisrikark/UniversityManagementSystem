from flask import render_template, request, jsonify, Blueprint
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import gridfs

filesAPI = Blueprint('filesAPI', __name__)

from myapp import app, client

db = client.eb
fs = gridfs.GridFS(db)

filesBase = '/files'

#################################### Helpers Beginning ####################################

def isEmpty(object):
    if(object is None):
        return True
    return False

######################################## Helpers Ending ###########################################

###################################### File API's Beginning #########################################

@filesAPI.route('/')
def index():
    return '''
        <form  method="POST" action="/files/storeFile" enctype="multipart/form-data">
            <input type="text" name="username">
            <input type="file" name="document">
            <input type="submit">
        </form>    
    '''


'''
    Explanation : 
        Send a file with "name" attribute "document"
        If there is a file in the request a response will be sent such as
        {
            "status" : "success",
            "id" : "fnue213iln4i347dsf"
        } 200
        If there is no file
        {
            "status" : "no file"
        } 400
'''
@filesAPI.route(filesBase + '/storeFile', methods=['POST'])
def storeFile():
    code = None
    response = {}
    if('document' in request.files):
        document = request.files['document']
        id = fs.put(document, filename=document.filename)
        code = 200
        response["status"] = "success"
        response["id"] = str(id)
        response["filename"] = str(document.filename)
    else:
        code = 400
        response["status"] = "no file sent"
    return jsonify(response), code

###################################### File API's Beginning #########################################