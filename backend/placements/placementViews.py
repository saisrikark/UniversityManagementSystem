from flask import Flask,jsonify,Blueprint
from flask import request,send_from_directory
placementAPI = Blueprint('placementAPI',__name__)
from myapp import app,client
import os,csv,requests,ast
ALLOWED_EXTENSIONS = set(['pdf','doc','txt']) 


db = client["placement_db"]


studentCollection = db["student"]
companyCollection = db["company"]
placementBase = "/api/v1/plac"

################################### HELPER BEGINNING ##############################
def student_database():
	studentList = [
	{"studentName":"Royal Mehta","studentId":"1234","semester":"8","section":"A","companies":[{"name":"Cure.fit","tier":"1"},{"name":"Cisco","tier":"1"},{"name":"Komprise","tier":"1"},{"name":"Tredence Analytics","tier":"2"}],"offers":[{"fulltime":"Komprise","internship":"Komprise"},{"fulltime":"Tredence Analytics","internship":"none"}]},
	{"studentName":"Sachin","studentId":"1235","semester":"8","section":"B","companies":[{"name":"Cure.fit","tier":"1"},{"name":"Exotel","tier":"1"},{"name":"Komprise","tier":"1"},{"name":"Standard Chartered","tier":"2"}],"offers":[{"fulltime":"Commvault","internship":"Commvault"}]},
	{"studentName":"Sai Srikar","studentId":"1236","semester":"8","section":"C","companies":[{"name":"Cure.fit","tier":"1"},{"name":"Cisco","tier":"1"},{"name":"Citrix","tier":"1"}],"offers":[{"fulltime":"Citrix","internship":"Citrix"}]},
	{"studentName":"Saloni Govil","studentId":"1237","semester":"8","section":"D","companies":[{"name":"Cure.fit","tier":"1"},{"name":"Cisco","tier":"1"},{"name":"Palo Alto","tier":"1"}],"offers":[{"fulltime":"Palo Alto","internship":"Palo Alto"}]},
	{"studentName":"Rahul Gupta","studentId":"1238","semester":"8","section":"E","companies":[{"name":"Cure.fit","tier":"1"},{"name":"Cisco","tier":"1"},{"name":"Palo Alto","tier":"1"}],"offers":"None"}
				]
	
	studentCollection.insert_many(studentList)
	
def company_database():
	companyList = [
	{"name":"Exotel","designation":"associate software engineer","companySector":"none-core","modeOfSelection":"interview","FT":"yes","internship":"yes","compensation":"17CTC","tier":"1","website":"exotel.com"},
	{"name":"Tredence Analytics","designation":"software engineer","companySector":"none-core","modeOfSelection":"interview","FT":"yes","internship":"no","compensation":"6.5CTC","tier":"2","website":"tredenceanalytics.com"},
	{"name":"Komprise","designation":"software test engineer","companySector":"none-core","modeOfSelection":"interview","FT":"yes","internship":"yes","compensation":"18CTC","tier":"1","website":"kommprise.com"},
	{"name":"Standard Chartered","designation":"software engineer","companySector":"none-core","modeOfSelection":"interview","FT":"yes","internship":"no","compensation":"6.1CTC","tier":"2","website":"standardchartered.com"},
	{"name":"Palo Alto","designation":"software engineer","companySector":"none-core","modeOfSelection":"interview","FT":"yes","internship":"yes","compensation":"22CTC","tier":"1","website":"paloalto.com"}
				  ]
	
	companyCollection.insert_many(companyList)
	
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
	
def isEmpty(object):
	if(object is None):
		return 	True
	else:
		return False

student_database()
company_database()
################################### HELPER ENDNING ##############################

################################### PLACEMENT API BEGINNING ##############################
#1)DETAILS OF COMPANY
@placementAPI.route(placementBase+"/compDetails",methods=['GET','POST'])
def compDetails():
	if request.method == 'POST':
		
		compName = request.json["name"]
		#print(compName)
		data = companyCollection.find_one({"name":compName})
		#print(data["name"])
		if data==None:
			msg = "Company details not found"
			return jsonify(msg),200
		new_data = {}
		new_data["name"] = data["name"]
		new_data["designation"] = data["designation"]
		new_data["companySector"] = data["companySector"]
		new_data["modeOfSelection"] = data["modeOfSelection"]
		new_data["FT"] = data["FT"]
		new_data["internship"] = data["internship"]
		new_data["compensation"] = data["compensation"]
		new_data["tier"] = data["tier"]
		new_data["website"] = data["website"]
	
		return jsonify(new_data),200
	else:
		msg = "Please select POST method"
		return jsonify(msg),405
#2)
@placementAPI.route(placementBase+"/name",methods=['GET','POST'])
def registeredCompanyName():
	if request.method == 'GET':
		studentId = request.args.get("studentId")
		
		data = studentCollection.find_one({"studentId":studentId})
		if data == None:
			msg = "incorrect studentId"
			return jsonify(msg),200
		return jsonify(data["companies"]),200
	else:
		msg = "please use GET method"
		return jsonify(msg),405		

#3)
@placementAPI.route(placementBase+"/totalComp",methods=['GET','POST'])
def tierWiseTotalCompany():
	if request.method == 'GET':
		tier1 = 0
		tier2 = 0
		tier3 = 0
		studentId = request.args.get("studentId")
		data = studentCollection.find_one({"studentId":studentId})
		#print("data is")
		#print(data)
		if data == None:
			msg = "incorrect studentId"
			return jsonify(msg),200
		for i in data["companies"]:
			if(i["tier"]=="1"):
				tier1 = tier1+ 1
			elif(i["tier"]=="2"):
				tier2 = tier2+ 1
			else:
				tier3 = tier3+ 1
		new_data = {}
		new_data["tier1"] = tier1
		new_data["tier2"] = tier2
		new_data["tier3"] = tier3
		
		
		return jsonify(new_data),200
	else:
		msg = "Please select GET method"
		return jsonify(msg),405	

#4)
@placementAPI.route(placementBase+"/FTofferName",methods=['GET','POST'])
def ftOfferedCompanyName():
	if request.method == 'GET':
		studentId = request.args.get("studentId")
		data = studentCollection.find_one({"studentId":studentId})
		if data == None:
			msg = "incorrect studentId"
			return jsonify(msg),200
		lis = []
		for i in data["offers"]:
			print(i["fulltime"])
			compName = i["fulltime"]
			data1 = companyCollection.find_one({"name":compName})
			if data1 == None:
				msg =compName + " company details not found"
				lis.append(msg)
				
				#return jsonify(msg),404
			else:
				new_data = {}
				
				new_data["companyName"] = data1["name"]
				new_data["type"] = data1["companySector"]
				new_data["tier"] = data1["tier"]
				new_data["CTC"]  = data1["compensation"]
				lis.append(new_data)
	
		return jsonify(lis),200
	else:
		msg = "Please select GET method"
		return jsonify(msg),405

#5)
@placementAPI.route(placementBase+"/internOfferName",methods=['GET','POST'])
def InternOfferedCompanyName():
	if request.method == 'GET':
		studentId = request.args.get("studentId")
		data = studentCollection.find_one({"studentId":studentId})
		#print(data)
		lis = []
		if data != None:
			for i in data["offers"]:
				compName = i["internship"]
				data1 = companyCollection.find_one({"name":compName})
				if compName == "none":
					msg = "Only full time offer given by " + i["fulltime"]
					lis.append(msg)
				elif data1 == None:
					msg = compName + " company details not found"
					lis.append(msg)
					break
				else:
					new_data = {}
					new_data["companyName"] = data1["name"]
					new_data["type"] = data1["companySector"]
					new_data["tier"] = data1["tier"]
					new_data["CTC"]  = data1["compensation"]
					lis.append(new_data)
			return jsonify(lis),200
		else:
			msg = "incorrect studentId"
			#print(msg)
			return jsonify(msg),200
	else:
		msg = "Please select GET method"
		return jsonify(msg),405
#6)
@placementAPI.route(placementBase+"/totalOffers",methods=['GET','POST'])
def totalJobOffers():
	if request.method == 'GET':
		ft = 0
		inter = 0
		studentId = request.args.get("studentId")
		data = studentCollection.find_one({"studentId":studentId})
		if data == None:
			msg = "incorrect studentId"
			return jsonify(msg),200
		for i in data["offers"]:
			if(i["fulltime"]!="none"):
				ft=ft+1
			if(i["internship"]!="none"):
				inter = inter + 1
		new_data = {}
		new_data["fullTime"] = ft
		new_data["internship"] = inter
		
		return jsonify(new_data),200
	else:
		msg = "please use GET method"
		return jsonify(msg),405
			
#7)RESUME UPLOAD
@placementAPI.route(placementBase+'/resumeUpload',methods=['GET','POST'])					
def upload_resume():
	if request.method == 'POST':
		
		if 'file' not in request.files:
			resp = jsonify('no file part in the request')
			resp.status_code = 400
			return resp
		resume = request.files['file']	
		#print(type(resume.filename))
		if resume.filename == '':
			resp = jsonify({'No file selected for uploading'})
			resp.status_code = 400
			return resp
		if allowed_file(resume.filename):
			resume.save(os.path.join(app.config['UPLOAD_FOLDER'],resume.filename))
			resp = jsonify('file uploaded successfully')
			resp.status_code = 201
			return resp
		else:
			resp = jsonify({'allowed file types are pdf,doc'})
			resp.status_code = 400
			return resp
	else:
		msg = 'please use POST method'
		return jsonify(msg),405	
		
#8)STUDENT REGISTER TO A PARTICULAR COMPANY
@placementAPI.route(placementBase+'/register/<company_name>',methods=['GET','POST'])
def register(company_name):
	if request.method == 'POST':
		studentName = request.form['studentName']
		studentId  = request.form['studentId']
		semester = request.form['semester']
		gpa = request.form['gpa']
		year = request.form['year']
		columnNames = ['studentName','studentId','semester','gpa','year']
		
		data = studentCollection.find_one({"studentId":studentId})
		if data == None:
			msg = "incorrect studentId"
			return jsonify(msg),400
		
		if data['offers'] != 'None':			
			return jsonify('Already have an offer')
		
		lis = data['companies']
		for i in lis:
			if i['name'] == company_name:
				return jsonify('Already registered')		
		
		if os.path.exists(company_name+'.csv')==False:
			
			f = open(company_name+'.csv','w')
			writer = csv.DictWriter(f,fieldnames=columnNames)
			writer.writeheader()
			writer.writerow({'studentName':studentName,'studentId':studentId,'semester':semester,'gpa':gpa,'year':year})
			f.close()
		else:
			#print("2")
			with open(company_name+'.csv','a') as  inFile:
				writer = csv.DictWriter(inFile,fieldnames=columnNames)
				writer.writerow({'studentName':studentName,'studentId':studentId,'semester':semester,'gpa':gpa,'year':year})
		
		data = studentCollection.find_one({"studentId":studentId})
	#	print(type(data['companies']))
		tier = companyCollection.find_one({"name":company_name})["tier"]
		studentCollection.update({"studentId":studentId},{'$push': {"companies":{"name":company_name,"tier":tier}}})
		return jsonify("thanks for registration")
	else:
		msg = 'please use POST method'
		return jsonify(msg),405	

#9)COMPNAY REGISTER TO OUR APP
@placementAPI.route(placementBase+'/companyRegister',methods=['GET','POST'])
def company_register():
		if request.method == 'POST':
			name = request.form['name']
			designation = request.form['designation']
			companySector = request.form['companySector']
			modeOfSelection = request.form['modeOfSelection']
			FT = request.form['FT']
			internship = request.form['internship']
			compensation = request.form['compensation']
			tier = request.form['tier']
			website = request.form['website']
			
			company_dict = {'name':name,'designation':designation,'copmanySector':companySector,'modeOfSelection':modeOfSelection,'FT':FT,'internship':internship,'compensation':compensation,'tier':tier,'website':website}
			companyCollection.insert_one(company_dict)
			
			return jsonify('Thanks for registring with us')
		else:
			msg = "pleae use POST method"
			return jsonify(msg),405

				
#10)download resume by the company
@placementAPI.route(placementBase+'/download/resume/<resume_name>',methods=['GET','POST'])
def donwload_resume(resume_name):
	try:
		return send_from_directory(app.config['UPLOAD_FOLDER'],filename=resume_name,as_attachment=True),200
	except FileNotFoundError:
		jsonify('resume not found'),404
		

#11)list of students registered to a company
@placementAPI.route(placementBase+'/list/<company_name>',methods=['GET','POST'])
def show_students_registered_to_company(company_name):
	try:
		with open(company_name + '.csv','r') as csv_file:
			csv_reader = csv.reader(csv_file,delimiter = ',')
			res = []
			for lines in csv_reader:
				res.append(lines[0])
		
			return jsonify(res[1:]),200	
	except FileNotFoundError:
		jsonify('no student registered yet'),400
		
#12)	
k = 1239		
@placementAPI.route(placementBase+'/getuser',methods=['GET','POST'])
def getuser():
	global k
	token = request.args.get('token')
	flg=0
	r = requests.get("http://localhost:5000/users/getUserByToken?token="+token)
	s = ast.literal_eval(r.text)
	#print(s["name"])
	
	data = list(studentCollection.find({},{"studentName":1}))
	#print(data)
	for i in data:
		if(i["studentName"]==s["name"]):
			flg=1
	if flg==0:
		studentName = s["name"]
		studentId = k
		semester = 8
		section = "F"
		companies = []
		offers = []
		k = k+1
		studentCollection.insert_one({"studentName":studentName,"studentId":studentId,"semester":semester,"section":section,"companies":companies,"offers":offers})
		return jsonify({"studentName":studentName,"studentId":studentId,"semester":semester,"section":section,"companies":companies,"offers":offers}),200
	
	res = list(studentCollection.find({"studentName":s["name"]}))
	data1 = res[0]
	return jsonify({"studentName":data1["studentName"],"studentId":data1["studentId"],"semester":data1["semester"],"section":data1["section"],"companies":data1["companies"],"offers":data1["offers"]}),200	
	
	
		