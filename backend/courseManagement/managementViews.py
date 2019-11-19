##### API's for course management adding to course etc ##########

from flask import render_template, request, jsonify, Blueprint, request, Flask

managementAPI = Blueprint('managementAPI',__name__)

from myapp import app, client
from pymongo import MongoClient

db = client.eb

courseManagementBase = '/courseManagement'

courseCollection = db.course_table
studentCollection = db.student_table
teacherCollection = db.teacher_table

'''
Create course
add teacher to course vice versa
add student to course vice versa
'''

@managementAPI.route(courseManagementBase +'/createCourse', methods=['POST'])
def createCourse():
    code = 200
    response = {}
    courseName = request.json['course_name']
    courseId = request.json['course_id']
    resp = courseCollection.insert({
        "course_id" : courseId,
        "course_name" : courseName,
        'teacher_ids' : [],
        'teacher_names' : [],
        'student_ids' : [],
        'student_names' : []
    })
    response['course_id'] = courseId
    response['course_name'] = courseName
    response['_id'] = str(resp)
    return response, code
    
#Adds teacher to course and vice versa
@managementAPI.route(courseManagementBase+'/teacherCourseAssociation', methods=['POST'])
def teacherCourseAssociation():
    teacherId = request.json['teacherId']
    courseId = request.json['courseId']
    #Fetching teacher and course
    teacher = teacherCollection.find({"teacher_id" : teacherId})
    course = courseCollection.find({"course_id" : courseId})
    ##Add teacher to course
    courseTeachers = course['teacher_ids']
    courseTeachersNames = course['teacher_names']
    if(teacherId not in courseTeachers):
        courseTeachers.append(teacherId)
        courseTeachersNames.append(teacher['t_name'])
    newvalues = { "$set": { "teacher_ids":courseTeachers,"teacher_names":courseTeachersNames}}
    courseCollection.update_one({"course_id" : courseId}, newvalues)
    ##Add course to teacher
    course_ids = teacher['course_ids']
    course_names = teacher['course_names']
    if(courseId not in course_ids):
        course_ids.append(courseId)
        course_names.append(course['course_name'])
    newvalues = {"$set" : {'course_ids' : course_ids, 'course_names' : course_names}}
    teacherCollection.update_one({"teacher_id" : teacherId}, newvalues)
    return jsonify({}), 200

@managementAPI.route(courseManagementBase+'/studentCourseAssociation', methods=['POST'])
def studentCourseAssociation():
    studentId = request.json['studentId']
    courseId = request.json['courseId']
    #Fetching teacher and course
    student = studentCollection.find({"studentId" : studentId})
    course = courseCollection.find({"course_id" : courseId})
    ##Add student to course
    courseStudents = course['student_ids']
    courseStudentNames = course['student_names']
    if(studentId not in courseStudents):
        courseStudents.append(studentId)
        courseStudentNames.append(student['studentName'])
    newvalues = { "$set": { "teacher_ids":courseStudents,"teacher_names":courseStudentNames}}
    courseCollection.update_one({"course_id" : courseId}, newvalues)
    ##Add course to student
    course_ids = student['course_ids']
    course_names = student['course_names']
    if(courseId not in course_ids):
        course_ids.append(courseId)
        course_names.append(course['course_name'])
    newvalues = {"$set" : {'course_ids' : course_ids, 'course_names' : course_names}}
    teacherCollection.update_one({"teacher_id" : student}, newvalues)
    return jsonify({}), 200
