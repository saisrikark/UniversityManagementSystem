##### API's for attendance ##########

from flask import render_template, request, jsonify, Blueprint, request, Flask

attendanceAPI = Blueprint('attendanceAPI',__name__)

from myapp import app, client
from pymongo import MongoClient

db = client.eb
coursesCollection = db.courses #courseID, courseName, teacherID, department
studentCollection = db.student #assuming all attributes are there
attendanceCollection = db.attendance_table
teachersCollection = db.teacher #teacherID, teacherName, department, courses

attendanceBase = "/csm/attendance"

################################################ API's beginning ##############################################
'''
    Takes a course code,
    a list of student_id's,
    and how many hours to update. 
'''
@attendanceAPI.route(attendanceBase + '/takeAttendance', methods=['POST'])
def takeAttendance():
    response = {}
    code = None
    c_id = request.json['c_id']
    studentList = request.json['s_list']
    hours = int(request.json['hrs'])
    for s_id in studentList:
        studentAttendance = attendanceCollection.find_one({"s_id" : s_id})
        if(studentAttendance is None):
             studentAttendance.insert({
                "s_id" : s_id,
                "attendance" : {
                    str(c_id) : [hours, hours]
                }})
        else:
           attendance = studentAttendance['attendance']
           try:
               attendance[c_id][0]+=hours
               attendance[c_id][1]+=hours
           except:
               attendance[c_id][0]=hours
               attendance[c_id][1]=hours
           response = attendanceCollection.find_one_and_replace({"s_id" : s_id},
           {"s_id" : s_id, "attendance" : attendance})
           response['_id'] = str(response['_id'])
        code = 200
    return jsonify(response), code

@attendanceAPI.route(attendanceBase + '/viewAttendance/<s_id>', methods=['GET'])
def viewAttendance(s_id):
    code = None
    studentAttendance = attendanceCollection.find_one({'s_id':s_id})
    if(s_id is ""):
        code=405
        studentAttendance = {}
    if(studentAttendance is None):
        code=404
        studentAttendance = {}
    else:
        studentAttendance['_id'] = str(studentAttendance['_id'])
        code = 200
    return studentAttendance, code
################################################ API's ending ##############################################
