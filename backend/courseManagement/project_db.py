from pymongo import MongoClient
client = MongoClient('mongodb+srv://srikar:srikar@cluster0-zhltr.mongodb.net/test?retryWrites=true&w=majority')
db = client.eb

#1.Student Collection
'''
Student collection schema
{
    "studentId : "12334",
    "studentName" : "dum dum",
    "semester" : 8,
    "section" : "A"
}
Changes - removed email and other unnecessary details which come in info of users.
'''
student_details = db.student_table
data1 = {"studentId" : "1234", 'studentName':'Rahul', "semester" : 8, "section" : "A"}
data2 = {"studentId" : "1234", 'studentName':'Rahul', "semester" : 8, "section" : "A"}
data3 = {"studentId" : "1234", 'studentName':'Rahul', "semester" : 8, "section" : "A"}
data4 = {"studentId" : "1234", 'studentName':'Rahul', "semester" : 8, "section" : "A"}
data5 = {"studentId" : "1234", 'studentName':'Rahul', "semester" : 8, "section" : "A"}
data6 = {"studentId" : "1234", 'studentName':'Rahul', "semester" : 8, "section" : "A"}
data7 = {"studentId" : "1234", 'studentName':'Rahul', "semester" : 8, "section" : "A"}
data8 = {"studentId" : "1234", 'studentName':'Rahul', "semester" : 8, "section" : "A"}
data9 = {"studentId" : "1234", 'studentName':'Rahul', "semester" : 8, "section" : "A"}
student_details.insert_many([data1,data2,data3,data4,data5,data6,data7,data8,data9])


#2.Courses Collection
'''
Mistakes in this
there can be many teachers for a course
Courses collection schema
{
    "courseId" : "2019CS001",
    "course_name" : "Software Engineering"
    "teacherIds" : ["TE001", "TE002", "TE003", "TE004"],
    "studentIds" : ["S001", "S002", "S003", "S004"]
}
'''
course_details = db.course_table
data1 = {'course_id':'2019CS001','course_name':'Software Engineering','teacherIds': ['TE001', 'TE002', 'TE003']}
data2 = {'course_id':'2019CS001','course_name':'Software Engineering','teacherIds': ['TE001', 'TE002', 'TE003']}
data3 = {'course_id':'2019CS001','course_name':'Software Engineering','teacherIds': ['TE001', 'TE002', 'TE003']}
data4 = {'course_id':'2019CS001','course_name':'Software Engineering','teacherIds': ['TE001', 'TE002', 'TE003']}
data5 = {'course_id':'2019CS001','course_name':'Software Engineering','teacherIds': ['TE001', 'TE002', 'TE003']}
data6 = {'course_id':'2019CS001','course_name':'Software Engineering','teacherIds': ['TE001', 'TE002', 'TE003']}
data7 = {'course_id':'2019CS001','course_name':'Software Engineering','teacherIds': ['TE001', 'TE002', 'TE003']}
data8 = {'course_id':'2019CS001','course_name':'Software Engineering','teacherIds': ['TE001', 'TE002', 'TE003']}
data9 = {'course_id':'2019CS001','course_name':'Software Engineering','teacherIds': ['TE001', 'TE002', 'TE003']}
course_details.insert_many([data1,data2,data3,data4,data5,data6,data7,data8,data9])


#3.Teachers Collection
''' 
Teachers collection schema
{
    'teacher_id':'TE001',
    't_name':'Ronak'
    'course_ids' : [],
    'course_names' : []
}
'''
teacher_details = db.teacher_table
data1 = {'teacher_id':'TE001','t_name':'Ronak'}
data2 = {'teacher_id':'TE002','t_name':'Ruchi'}
data3 = {'teacher_id':'TE003','t_name':'Rajesh'}
data4 = {'teacher_id':'TE004','t_name':'Sachit'}
data5 = {'teacher_id':'TE005','t_name':'Roopa'}
data6 = {'teacher_id':'TE006','t_name':'Seema'}
teacher_details.insert_many([data1,data2,data3,data4,data5,data6])

#4.Attendance Collection
'''
Attendance collection schema
{
    "student_id" : "ST001",
    "attendance" :
    {
        "c_id1": [3:10], //Attended 3/10
        "c_id2": [4:12]
    }
}
'''
attendance_details = db.attendance_table
data1 = {'s_id':'ST001','attendance': {'c_id1':[1,2], 'c_id2':[1,2]}}
data2 = {'s_id':'ST001','attendance': {'c_id1':[1,2], 'c_id2':[1,2]}}
data3 = {'s_id':'ST001','attendance': {'c_id1':[1,2], 'c_id2':[1,2]}}
data4 = {'s_id':'ST001','attendance': {'c_id1':[1,2], 'c_id2':[1,2]}}
attendance_details.insert_many([data1,data2,data3,data4])

#5.Material Collection
'''
Material collection schema
{
    'course_id':'2019CS001',
    'title':'SCRUM',
    'desc':'Scrum is an agile process framework for managing complex knowledge.',
    "filename" : "bumbum.pdf"
}

'''
material_details = db.material_table
data1 = {'course_id':'2019CS001','title':'SCRUM',
'desc':'Scrum is an agile process framework for managing complex knowledge.', "filename" : "bumbum.pdf"}
data2 = {'course_id':'2019CS001','title':'AGILE',
'desc':'Requirements and solutions evolve through the collaborative effort.',  "filename" : "bumbum.pdf"}
data3 = {'course_id':'2019CS002','title':'BUBBLE SORT',
'desc':'Repeatedly swapping the adjacent elements if they are in wrong order.',  "filename" : "bumbum.pdf"}
data4 = {'course_id':'2019CS002','title':'HEAPSORT',
'desc':'Comparison-based sorting algorithm.',  "filename" : "bumbum.pdf"}
data5 = {'course_id':'2019CS003','title':'AJAX',
'desc':'Helps create asynchronous web applications.',  "filename" : "bumbum.pdf"}
data6 = {'course_id':'2019CS004','title':'ARRAYS',
'desc':'Collection of elements, each identified by an index',  "filename" : "bumbum.pdf"}
material_details.insert_many([data1,data2,data3,data4,data5,data6])

#6.Assignment Collection
'''
Assignment collection schema
{
    'course_id':'2019CS001',
    'a_id':'ASS001',
    'ques':'Assignment question SE1',
    'exp':'SE Assignment 1 description here.',
    'deadline':'12/09/2019',
    'filename' : 'shakalakalaka.docx'
}
'''
assignment_details = db.assignment_table
data1 = {'course_id':'2019CS001','a_id':'ASS001','ques':'Assignment question SE1',
'exp':'SE Assignment 1 description here.','deadline':'12/09/2019', 'filename' : 'shakalakalaka.docx'}
data2 = {'course_id':'2019CS001','a_id':'ASS001','ques':'Assignment question SE1',
'exp':'SE Assignment 1 description here.','deadline':'12/09/2019', 'filename' : 'shakalakalaka.docx'}
data3 = {'course_id':'2019CS001','a_id':'ASS001','ques':'Assignment question SE1',
'exp':'SE Assignment 1 description here.','deadline':'12/09/2019', 'filename' : 'shakalakalaka.docx'}
assignment_details.insert_many([data1,data2,data3])

#7.Assignments Submitted Collection
'''
{
    'studentId' : '12345678999999',
    'studentName' : 'Cowboy Bebop',
    'a_id' : '12345678', 
    'filename' : 'copied.txt'
    'marks' : '10/10'
}
'''
data1 = {'studentId' : '12345678999999', 'studentName' : 'Cowboy Bebop', 'a_id' : '12345678', 'filename' : 'copied.txt',
 'marks' : '10/10'}
data2 = {'studentId' : '12345678999999', 'studentName' : 'Cowboy Bebop', 'a_id' : '12345678', 'filename' : 'copied.txt',
 'marks' : '10/10'}
data3 = {'studentId' : '12345678999999', 'studentName' : 'Cowboy Bebop', 'a_id' : '12345678', 'filename' : 'copied.txt',
 'marks' : '10/10'}
data4 = {'studentId' : '12345678999999', 'studentName' : 'Cowboy Bebop', 'a_id' : '12345678', 'filename' : 'copied.txt',
 'marks' : '10/10'}
data5 = {'studentId' : '12345678999999', 'studentName' : 'Cowboy Bebop', 'a_id' : '12345678', 'filename' : 'copied.txt',
 'marks' : '10/10'}
data6 = {'studentId' : '12345678999999', 'studentName' : 'Cowboy Bebop', 'a_id' : '12345678', 'filename' : 'copied.txt',
 'marks' : '10/10'}
submittedAssignments = db.submitted_assignments
submittedAssignments.insert_many([data1, data2, data3, data4, data5, data6])