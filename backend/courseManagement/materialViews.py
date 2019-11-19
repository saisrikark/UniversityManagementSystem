########### Material API's ############

from flask import render_template, request, jsonify, Blueprint, request, Flask
from bson.objectid import ObjectId
import gridfs

materialAPI = Blueprint('materialAPI',__name__)

from myapp import app, client
from pymongo import MongoClient

db = client.eb
coursesCollection = db.courses
courseMaterialCollection = db.material_table
fs = gridfs.GridFS(db)

studyMaterialBase = "/csm/studymaterial"

def isEmpty(Object):
    if(Object is None):
        return True
    return False

################################################ API's beginning ##############################################

@materialAPI.route(studyMaterialBase + '/uploadMaterial', methods=['POST'])
def uploadMaterial():
    code = None
    response = {}
    courseID = request.json['course_id']
    materialDescription = request.json['desc']
    title = request.json['title']
    filename = request.json['filename']
    response = courseMaterialCollection.insert(
        {"course_id":courseID, "desc":materialDescription,
        "title":title, "filename":filename
        })
    if(response is None):
        code = 400
        response = {"status" : "faliure"}
    else:
        code = 200
        response = {"status" : "success"}
    return response, code


'''
Search material will not return the file but will return the metadata.
Use the metadata to make another call to fetch the file.
'''
@materialAPI.route(studyMaterialBase+'/search/<string:course_id>', methods=['GET'])
def searchMaterialByCourseId(course_id):
    res = courseMaterialCollection.find(
         {'course_id': course_id} )
    if(not res):
        return jsonify({}), 400
    materials = list()
    for i in res:
        i['_id'] = str(i['_id'])
        materials.append(i)
    return jsonify(materials), 200


@materialAPI.route(studyMaterialBase+'/delete/<string:mId>', methods=['DELETE'])
def deleteMaterial(mId):
    code = None
    res = list(courseMaterialCollection.find(
         {'_id': ObjectId(mId)} ))
    if(len(res)==0):
        code = 404
    else:
        for i in res:
            print(i)
            courseMaterialCollection.find_one_and_delete({'_id': i['_id']})
            if(i['filename'] != '*'):
                for grid_out in fs.find({"filename": i["filename"]}, no_cursor_timeout=True):
                    fs.delete(grid_out._id)
        code = 200
    return jsonify({}), code
################################################ API's ending ##############################################