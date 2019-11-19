import json
import unittest
from flask import request


from myapp import app,client


#db = client["placements1"]


class BasicTest(unittest.TestCase):
	
	#runs before every test case
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['DEBUG'] = False
		self.app = app.test_client()
		#print("set up")
	
	#runs after every test case	
	def tearDown(self):
		#print("tear down")
		pass
		
	####################  HELPERS   STARTING #####################
	##############################################################
	def helper1(self,dummy,usn):
		return self.app.post('/api/v1/plac/{}?studentId={}'.format(dummy,usn),follow_redirects=True)
	def helper2(self,dummy,usn):
		return self.app.get('/api/v1/plac/{}?studentId={}'.format(dummy,usn),follow_redirects=True)
		
	def help1_compDetails(self,name):
		return self.app.get('/api/v1/plac/compDetails',follow_redirects=True)
	def help2_compDetails(self,name):
		return self.app.post('/api/v1/plac/compDetails',data=json.dumps({"name":"{}".format(name)}),content_type='application/json')
	

    #####################  HEPERS ENDING    ######################
    ##############################################################
	
	
	#####################  TEST FUNCTIONS STARTING  ##############
	##############################################################
	
	#API_1)	
	def test_totalComp(self):
		##TC1: wrong method
		response = self.helper1('totalComp','1234')
		self.assertEqual(response.status_code,405)
		self.assertIn(b'GET',response.data)
		
		##TC2: correct output
		response = self.helper2('totalComp','1234')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'{"tier1":3,"tier2":1,"tier3":0}',response.data)
		
		##TC3: incorrect USN
		response = self.helper2('totalComp','124')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'incorrect studentId',response.data)
	
	#API_2)	
	def test_compDetails(self):
		##TC1: wrong method
		response = self.help1_compDetails('Komprise')
		self.assertEqual(response.status_code,405)
		self.assertIn(b'POST',response.data)
		
		##TC2: correct output
		response = self.help2_compDetails('Komprise')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'Komprise',response.data)
		
		##TC3: invalid name
		response = self.help2_compDetails('Adobe')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'Company details not found',response.data)
	
	#API_3)
	def test_name(self):
		##TC1: wrong method
		response = self.helper1('name','01FB16ECS323')
		self.assertEqual(response.status_code,405)
		self.assertIn(b'GET',response.data)
		
		
		##TC2: incorrect USN
		response = self.helper2('name','01FB16ECS324')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'incorrect studentId',response.data)	
	
	#API_4)
	def test_FTofferName(self):
		##TC1: wrong method
		response = self.helper1('FTofferName','1234')
		self.assertEqual(response.status_code,405)
		self.assertIn(b'GET',response.data)
		
		##TC2: offered company details not stored in the database
		response = self.helper2('FTofferName','1235')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'company details not found',response.data)
		
		##TC3: invalid USN
		response = self.helper2('FTofferName','1223')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'incorrect studentId',response.data)
		
	#API_5)
	def test_internOfferName(self):
		##TC1: wrong method
		response = self.helper1('internOfferName','1234')
		self.assertEqual(response.status_code,405)
		self.assertIn(b'GET',response.data)
		
		##TC2: offered company details not stored in the database
		response = self.helper2('internOfferName','1235')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'company details not found',response.data)
		
		##TC3: invalid USN
		response = self.helper2('internOfferName','1223')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'incorrect studentId',response.data)
	
	
	#API_6)
	def test_totalOffers(self):
		##TC1: wrong method
		response = self.helper1('totalOffers','1234')
		self.assertEqual(response.status_code,405)
		self.assertIn(b'GET',response.data)
		
		##TC2: coorect output
		response = self.helper2('totalOffers','1234')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'fullTime',response.data)
		
		##TC3: invalid USN
		response = self.helper2('totalOffers','1225')
		self.assertEqual(response.status_code,200)
		self.assertIn(b'incorrect studentId',response.data)
	
	################### TEST FUNCTIONS ENDING  ###################
	##############################################################	
		
		

if __name__ == "__main__":
	unittest.main()