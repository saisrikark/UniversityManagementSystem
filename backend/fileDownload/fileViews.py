from flask import render_template, request, jsonify, Blueprint
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import gridfs

filesAPI = Blueprint('filesAPI', __name__)

from myapp import app

app.config['MONGO_URI'] = 'mongodb+srv://srikar:srikar@cluster0-zhltr.mongodb.net/test?retryWrites=true&w=majority/eb'
mongo = PyMongo(app)    

filesBase = '/files'

#################################### Helpers Beginning ####################################

def isEmpty(object):
    if(object is None):
        return True
    return False

######################################## Helpers Ending ###########################################

###################################### File API's Beginning #########################################

'''
    Explanation :
    Send a get request with the id you got from storing the file

'''
@filesAPI.route(filesBase + '/receiveFile/<id>', methods=['GET'])
def receiveFile(id):
    filename = id
    #out = fs.get(ObjectId(id))
    #filename = out.filename
    try :
        return mongo.send_file(filename, base="fs", version=-1)
    except:
        return jsonify("No such file"), 404
###################################### File API's Beginning #########################################