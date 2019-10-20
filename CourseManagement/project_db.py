from pymongo import MongoClient
client = MongoClient()
db = client['course_management_db']

#1.Student Collection
student_details = db.student_table
data1 = {'student_id':'ST001','s_name':'Rahul','s_contact':'8887712120','s_email':'rahul@gmail.com','section':'5A'}
data2 = {'student_id':'ST002','s_name':'Raghav','s_contact':'8898513120','s_email':'raghav123@gmail.com','section':'5B'}
data3 = {'student_id':'ST003','s_name':'Sagar','s_contact':'9992212120','s_email':'sagar@gmail.com','section':'5C'}
data4 = {'student_id':'ST004','s_name':'Ashu','s_contact':'8892267120','s_email':'ashu12@gmail.com','section':'5A'}
data5 = {'student_id':'ST005','s_name':'Ashish','s_contact':'8792212039','s_email':'ashish67@gmail.com','section':'7A'}
data6 = {'student_id':'ST006','s_name':'Alisha','s_contact':'8555755287','s_email':'alisha26@gmail.com','section':'7B'}
data7 = {'student_id':'ST007','s_name':'Ayushi','s_contact':'9430712120','s_email':'ayushi@gmail.com','section':'7A'}
data8 = {'student_id':'ST008','s_name':'Deepika','s_contact':'9835513120','s_email':'deepika007@gmail.com','section':'7C'}
data9 = {'student_id':'ST009','s_name':'Purva','s_contact':'9939212120','s_email':'purva001@gmail.com','section':'7B'}
student_details.insert_many([data1,data2,data3,data4,data5,data6,data7,data8,data9])


#2.Courses Collection
course_details = db.course_table
data1 = {'course_id':'2019CS001','course_name':'Software Engineering','teacher_id':'TE001'}
data2 = {'course_id':'2019CS001','course_name':'Software Engineering','teacher_id':'TE002'}
data3 = {'course_id':'2019CS002','course_name':'Algorithms','teacher_id':'TE003'}
data4 = {'course_id':'2019CS002','course_name':'Algorithms','teacher_id':'TE001'}
data5 = {'course_id':'2019CS003','course_name':'Web Technology','teacher_id':'TE004'}
data6 = {'course_id':'2019CS003','course_name':'Web Technology','teacher_id':'TE005'}
data7 = {'course_id':'2019CS004','course_name':'Data Structures','teacher_id':'TE002'}
data8 = {'course_id':'2019CS004','course_name':'Data Structures','teacher_id':'TE005'}
data9 = {'course_id':'2019CS004','course_name':'Data Structures','teacher_id':'TE006'}
course_details.insert_many([data1,data2,data3,data4,data5,data6,data7,data8,data9])


#3.Teachers Collection
teacher_details = db.teacher_table
data1 = {'teacher_id':'TE001','t_name':'Ronak','t_email':'ronak@gmail.com'}
data2 = {'teacher_id':'TE002','t_name':'Ruchi','t_email':'ruchi@gmail.com'}
data3 = {'teacher_id':'TE003','t_name':'Rajesh','t_email':'rajesh@gmail.com'}
data4 = {'teacher_id':'TE004','t_name':'Sachit','t_email':'sachit@gmail.com'}
data5 = {'teacher_id':'TE005','t_name':'Roopa','t_email':'roopa@gmail.com'}
data6 = {'teacher_id':'TE006','t_name':'Seema','t_email':'seema@gmail.com'}
teacher_details.insert_many([data1,data2,data3,data4,data5,data6])

#4.Attendance Collection
attendance_details = db.attendance_table
data1 = {'student_id':'ST001','section':'5A','c_id1':'2019CS002', 'c_id2':'2019CS004'}
data2 = {'student_id':'ST002','section':'5B','c_id1':'2019CS002', 'c_id2':'2019CS004'}
data3 = {'student_id':'ST003','section':'5C','c_id1':'2019CS002', 'c_id2':'2019CS004'}
data4 = {'student_id':'ST004','section':'5A','c_id1':'2019CS002', 'c_id2':'2019CS004'}
data5 = {'student_id':'ST005','section':'7A','c_id1':'2019CS001', 'c_id2':'2019CS003'}
data6 = {'student_id':'ST006','section':'7B','c_id1':'2019CS001', 'c_id2':'2019CS003'}
data7 = {'student_id':'ST007','section':'7A','c_id1':'2019CS001', 'c_id2':'2019CS003'}
data8 = {'student_id':'ST008','section':'7C','c_id1':'2019CS001', 'c_id2':'2019CS003'}
data9 = {'student_id':'ST009','section':'7B','c_id1':'2019CS001', 'c_id2':'2019CS003'}
attendance_details.insert_many([data1,data2,data3,data4,data5,data6,data7,data8,data9])
