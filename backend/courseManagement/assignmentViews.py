####### Assignment API's #############

from flask import render_template, request, jsonify, Blueprint, request, Flask
import gridfs

assignmentAPI = Blueprint('assignmentAPI',__name__)

from myapp import app, client
from pymongo import MongoClient
from flask_pymongo import PyMongo

assignmentsBase = "/csm/assignments"
#mongo = PyMongo(assignmentAPI)
mongo = MongoClient()


db = client.eb
assignmentCollection = db.assignment_table
submittedAssignmentsCollection = db.submitted_assignments

fs = gridfs.GridFS(db)

def isEmpty(Object):
    if(Object is None):
        return True
    return False

################################################ API's beginning ##############################################

@assignmentAPI.route(assignmentsBase+'/view/<string:courseID>', methods=['GET'])
def viewAssignments(courseID):
    res = list(assignmentCollection.find(
         {'course_id': courseID} ))
    if(isEmpty(res)):
        return jsonify({}), 400
    assignments = list()
    for i in res:
        i['_id'] = str(i['_id'])
        assignments.append(i) 
    return jsonify(assignments), 200


@assignmentAPI.route(assignmentsBase+'/submit', methods=['POST'])
def submitAssignments():
    submittedAssignmentsCollection.insert(
        {'studentName': request.json['studentName'],
        'studentId': request.json['studentId'],
        'filename': request.json['filename'], 'marks' : '', 
        'a_id' : request.json['a_id']})
    return jsonify({}), 200
    

@assignmentAPI.route(assignmentsBase+'/gradeAssignment', methods=['POST'])
def gradeAssignment():
    code = None
    a_id = request.json['a_id']
    marks = request.json['marks']
    res = submittedAssignmentsCollection.find_one_and_update(
        {'a_id' : a_id}, {'$set' : {'marks' : marks}})
    if(res is None):
        res = {}
        code = 400
    else:
        res['_id'] = str(res['_id'])
        res['marks'] = marks
    return jsonify(res), code


@assignmentAPI.route(assignmentsBase+'/viewgrades/<string:studentId>', methods=['GET'])
def viewAssignmentGrades(studentId):
    code = None
    resp = submittedAssignmentsCollection.find({
        'studentId':studentId})
    l = []
    if(not resp):
        resp = {}
        code = 405
    else:
        for i in resp:
            i['_id'] = str(i['_id'])
            l.append(i)
        code=200
    return jsonify(l), code

@assignmentAPI.route(assignmentsBase+'/create', methods=['POST'])
def createAssignment():
    response = {}
    code = None
    courseId = request.json['course_id']
    a_id = request.json['a_id']
    ques = request.json['ques']
    exp = request.json['exp']
    deadline = request.json['deadline']
    filename = request.json['filename']
    if(not assignmentCollection.find_one({'course_id' : courseId}) is None):
        code=400
    else:
        assignmentCollection.insert_one({
            'course_id' : courseId, 'a_id' : a_id,
            'ques' : ques, 'exp' : exp, 'deadline' : deadline,
            'filename' : filename
        })
        response['status'] = 'success'
        code=201
    return jsonify(response), code
################################################ API's ending ##############################################