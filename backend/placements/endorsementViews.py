from flask import Flask,jsonify,Blueprint
from flask import request
endorsementAPI = Blueprint('endorsementAPI',__name__)
from myapp import app,client


db = client.placements
endorsementsBase = "/api/v1/plac"

'''
    Endorsement collection example
    {
        "s_id" : "12121212121212",
        "skills" : [
            "skillname" : {
                "desc" : "some description",
                "endorsements" : ["Teacher name1", "Teacher name2"]
            }
        ]
    }
'''

@endorsementAPI.route('/addSkill', methods=['POST'])
def addSkill():
    pass

@endorsementAPI.route('/removeSkill', methods=['POST'])
def removeSkill():
    pass

@endorsementAPI.route('/endorseSkill', methods=['POST'])
def endorseSkill():
    pass