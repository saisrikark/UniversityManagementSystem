############################################## Plagiarism Checking API##########################################

from flask import render_template, request, jsonify, Blueprint, request, Flask
from re import split
import gridfs

plagiarismCheckAPI = Blueprint('plagiarismCheckAPI',__name__)

from myapp import app, client
from pymongo import MongoClient

assignmentsBase = '/csm/assignments'

regex = '; |. |, '

db = client.eb
fs = gridfs.GridFS(db)
submittedAssignmentsCollection = db.submitted_assignments

################################################ Helpers beginning ##############################################
def isEmpty(object):
    if(object is None):
        return True
    return False

def splitTextOnCondition(docList):
    # Split the eniter document which has been extracted to text, according to the regex
    length = len(docList)
    for i in range(length):
        docList[i] = split(regex, docList[i])
    return docList

def convertToText():
    #Irrespective of the file type : pdf, txt or docx
    #Convert to text type and send
    #Does not split
    '''TO BE IMPLEMENTED'''
    '''As of now not implmenting'''
    return "text"

def returnAllTextFromFile(filenameList):
    #Takes a list of filenames and returns all the documents in text format
    #Call convertToText for conversion
    fileList = []
    for filename in filenameList:
        for grid_out in fs.find({"filename": filename},
        no_cursor_timeout=True):
            data = grid_out.read()
            fileList += data.decode("utf-8")
    return fileList

def getAllDocsTextAndUserId(assignId):
    # retreive all documents for the given assignmentId
    code = None
    filenameList = []
    usernameList = []
    mongoResponse = submittedAssignmentsCollection.find({"a_id" : assignId})
    # Fetching all the records for given assignment
    if(not isEmpty(mongoResponse)):
        code = 200
        #We need filename to access the file on GridFs
        for i in mongoResponse:
            filenameList.append(i["filename"])
            usernameList.append(i["studentName"])
        fileList = returnAllTextFromFile(filenameList)
        return fileList, usernameList, code
    else:
        code = 400
        return [], [], code

def returnSimilarity(textList1, textList2):
    #Returns similarilty between two documents
    #Each testList will already be split according to the regex
    ''' 
        Logic
        1. Finding how much difference is there between two sets.
        2. Length of the difference set by the max length of both sets
        is the current similarity cost.
    '''
    textList1 = set(textList1)
    textList2 = set(textList2)
    difference = textList1 - textList2
    diffLen = len(difference)
    similarity = diffLen / max(len(textList1), len(textList2))
    return similarity

def generateSimilarityResponse(docSplitList, studentIdList):
    response = {}
    length = len(studentIdList)
    for i in range(length):
        for j in range(i+1, length):
            response[[i,j]] = returnSimilarity(docSplitList[i], docSplitList[j])
    return response
################################################ Helpers ending #################################################




################################################ API's beginning ##############################################
@plagiarismCheckAPI.route(assignmentsBase + '/plagiarismCheck', methods=['GET'])
def plagiarismCheck(assignId):
    code = None
    response = {}
    response["assignId"] = assignId
    docListSplit, studentIdList, code = getAllDocsTextAndUserId(assignId)
    similarityResponse = generateSimilarityResponse(
        docListSplit, studentIdList)
    response["similarity"] = similarityResponse
    return jsonify(response), code
'''
     Gets an assignment id as argument input
     For that assignment id -> find the corresponding submissions
     Take each document - perform splits on the text 
     Store each document's splits in a list
     Perform bubble sort like comparision on each document with the other document
     Give the result. what format ?
     Result format:
     {
         assignId : 12345,
         {
             ["studentname1", "studentname2"] : correspondingSimilarity1,
             ["studentname1", "studentname3"] : correspondingSimilarity2,
             ["studentname2", "studentname3"] : correspondingSimilarity3
         }
     }
    '''
################################################ API's ending #################################################