import json
import unittest
from flask import request


from myapp import app,client


db = client.eb
blogArticleCollection=db.blog


class BasicTest(unittest.TestCase):
	
	#runs before every test case
	def setUp(self):
		resource=blogArticleCollection.find_one()
		resourceId=str(resource["_id"])
		usrId=resource["ownerId"]
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
	def help1(self,dummy):
		return self.app.post('/blog/{}'.format(dummy),follow_redirects=True)

	def help2(self,dummy):
		return self.app.get('/blog/{}'.format(dummy),follow_redirects=True)
	
	def helper1(self,dummy,usn):
		return self.app.post('/blog/{}/{}'.format(dummy,usn),follow_redirects=True)
	def helper2(self,dummy,usn):
		return self.app.get('/blog/{}/{}'.format(dummy,usn),follow_redirects=True)


	def help1_upvote(self,userId,resourceId):
		return self.app.get('/blog/upvoteblog',follow_redirects=True)
	def help2_upvote(self,userId,resourceId):
		return self.app.post('/blog/upvoteblog',data=json.dumps({"userId":"{}".format(userId),"resourceId":"{}".format(resourceId)}),content_type='application/json')

	def help1_downvote(self,userId,resourceId):
		return self.app.get('/blog/downvoteblog',follow_redirects=True)
	def help2_downvote(self,userId,resourceId):
		return self.app.post('/blog/downvoteblog',data=json.dumps({"userId":"{}".format(userId),"resourceId":"{}".format(resourceId)}),content_type='application/json')

	def help1_comm(self,comments,resourceId):
		return self.app.get('/blog/commentonarticle',follow_redirects=True)
	def help2_comm(self,comments,resourceId):
		return self.app.post('/blog/commentonarticle',data=json.dumps({"comments":"{}".format(comments),"resourceId":"{}".format(resourceId)}),content_type='application/json')
		
	def help1_searchArt(self,searchString):
		return self.app.get('/blog/searchArticle',follow_redirects=True)
	def help2_searchArt(self,searchString):
		return self.app.post('/blog/searchArticle',data=json.dumps({"searchString":"{}".format(searchString),"resourceId":294664}),content_type='application/json')
	

    #####################  HEPERS ENDING    ######################
    ##############################################################
	
	
	#####################  TEST FUNCTIONS STARTING  ##############
	##############################################################
	#5dd2e9dd28edbdbf84a1916f
	#API_1)	
	def test_getAllArticles(self):
		##TC1: wrong method
		response = self.help1('getAllArticles')
		self.assertEqual(response.status_code,405)
		self.assertIn(b'GET',response.data)
		
		#TC2: correct output
		response = self.help2('getAllArticles')
		self.assertEqual(response.status_code,200)
		self.assertIn(response.data,response.data)

	def test_searchArtciles(self):
		##TC1: wrong method
		response = self.help1_searchArt('animantion')
		self.assertEqual(response.status_code,405)
        #self.assertIn(b'POST',response.data)
		
		##TC2: correct output
		response = self.help2_searchArt('cricket')
		self.assertEqual(response.status_code,200)
		#self.assertIn(b'',response.data)
		
		##TC3: invalid name
		response = self.help2_searchArt('food')
		self.assertEqual(response.status_code,400)
		self.assertIn(b'no articles found',response.data)
	
	#API_3)
	def test_commenting(self):
		##TC1: wrong method
		resource=blogArticleCollection.find_one()
		resourceId=str(resource["_id"])

		response = self.help1_comm('Beautiful',resourceId)
		self.assertEqual(response.status_code,405)
		#self.assertIn(b'GET',response.data)
		
		
		##TC2: correct output
		response = self.help2_comm('Legendary',resourceId)
		self.assertEqual(response.status_code,200)
		#self.assertIn(b'{}',response.data)	

		#TC3: Article not found
		response=self.help2_comm("Gameboy",'5dd2e9dd28edbdbf84a1619f')
		self.assertEqual(response.status_code,404)
		self.assertIn(b'article not found',response.data)
	
	#API_4)
	def test_upvoting(self):
		resource=blogArticleCollection.find_one()
		resourceId=str(resource["_id"])
		##TC1: wrong method
		response = self.help1_upvote('user123',resourceId)
		self.assertEqual(response.status_code,405)
		#self.assertIn(b'GET',response.data)
		
		##TC2: correct output
		response = self.help2_upvote('user123',resourceId)
		self.assertEqual(response.status_code,200)
		#self.assertIn(b'company details not found',response.data)
		
		##TC3: invalid Article id/Not found
		response = self.help2_upvote('user123','5dd2e9dd28edbdbf84a1619f')
		self.assertEqual(response.status_code,404)
		self.assertIn(b'article not found',response.data)
		
	#API_5)
	def test_downvote(self):
		resource=blogArticleCollection.find_one()
		resourceId=str(resource["_id"])

		##TC1: wrong method
		response = self.help1_downvote('user123',resourceId)
		self.assertEqual(response.status_code,405)
		#self.assertIn(b'GET',response.data)
		
		##TC2: correct output
		response = self.help2_downvote('user123',resourceId)
		self.assertEqual(response.status_code,200)
		#self.assertIn(b'company details not found',response.data)
		
		##TC3: invalid Article id/Not found
		response = self.help2_downvote('user123','5dd2e9dd28edbdbf84a1619f')
		self.assertEqual(response.status_code,404)
		self.assertIn(b'article not found',response.data)
	
	
	#API_6)
	def test_getByUserId(self):
		resource=blogArticleCollection.find_one()
		usrId=resource["ownerId"]
		##TC1: wrong method
		response = self.helper1('getByUserId',usrId)
		self.assertEqual(response.status_code,405)
		#self.assertIn(b'GET',response.data)
		
		##TC2: corect output
		response = self.helper2('getByUserId',usrId)
		self.assertEqual(response.status_code,200)
		#self.assertIn(b'fullTime',response.data)
		
		##TC3: invalid User Id
		response = self.helper2('getByUserId','user321')
		self.assertEqual(response.status_code,400)
		self.assertIn(b'article not found or invalid userid',response.data)
	
	################### TEST FUNCTIONS ENDING  ###################
	##############################################################	
		
		

if __name__ == "__main__":
	unittest.main()