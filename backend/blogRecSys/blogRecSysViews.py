from flask import render_template, request, jsonify, Blueprint, send_from_directory
from bson.objectid import ObjectId

blogRecSysAPI = Blueprint('blogRecSysAPI', __name__)

import os,csv,requests,ast
from myapp import app, client
from random import randint, seed
from time import time
import datetime


blogBase = '/blog'
recSysBase = '/recSys'

db = client.eb
blogArticleCollection = db.blog

#################################### Helpers Beginning ####################################

def isEmpty(object):
    if(object is None):
        return True
    return False

######################################## Helpers Ending ###########################################

###################################### Blog API Beginning #########################################

@blogRecSysAPI.route(blogBase + '/createBlogArticle', methods = ['POST'])
def createBlogArticle():
    response = {}
    title = request.json["title"]
    tags = request.json["tags"]
    ownerId = request.json["ownerId"] #Send token here
    category = request.json["category"] 
    info = request.json["info"]
    #token = request.json["token"]
    ##Authorization functionality
    ##Check if user is logged in 
    '''Insert here'''
    ##End here
    code = None
    seed()
    comments = []
    commentsUploadTime = []
    timeUploaded = time()
    upvotes = 0
    upvotersId = []
    downvotes = 0
    downvotersId = []
    if(len(tags) == 0):
        tags.add("generic")
    mongoResponse = blogArticleCollection.insert({
        "title" : title, "tags" : tags,
        "ownerId" : ownerId, "category" : category, "info" : info,
        "comments" : comments, "commentsUploadTime" : commentsUploadTime,
        "timeUploaded" : timeUploaded,
        "upvotes" : upvotes, "upvotersId" : upvotersId,
        "downvotes" : downvotes, "downvotersId" : downvotersId
    })
    response = {"_id" : str(mongoResponse)}
    return jsonify(response),code

@blogRecSysAPI.route(blogBase + '/deleteBlogArticle', methods = ['POST'])
def deleteBlogArticle():
    code = None
    response = {}
    #userId = request.json["userId"]
    #token = request.json["token"]
    resourceId = request.json["resourceId"]
    #operation = 'D'
    '''
        Insert authorization code here
    '''
    mongoResponse = blogArticleCollection.find_one(
        {"_id" : ObjectId(resourceId)})
    if(isEmpty(mongoResponse)):
        code = 404
        response = {"res" : "Not Found"}
    else:
        code = 200
        blogArticleCollection.delete_one(
            {"_id" : ObjectId(resourceId)})
        response = {"res" : "Deleted"}
    return jsonify(response), code

@blogRecSysAPI.route(blogBase + '/getByUserId/<string:userId>', methods = ['GET'])
def getArticlesByUserId(userId):
    code = None
    mongoResponse = list(blogArticleCollection.find({"ownerId" : userId}))
    response = list()
    for i in mongoResponse:
        tempDict = dict()
        for key in i:
            tempDict[key] = i[key]
        response.append(tempDict)
        del tempDict['_id']
    if(not len(response)):
        code = 400
        response="article not found or invalid userid"
    else:
        code = 200
    return jsonify(response), code


@blogRecSysAPI.route(blogBase + '/upvoteblog', methods = ['POST'])
def upvoteBlogArticle():
    code = None
    response={}
    userId = request.json["userId"]
    resourceId = request.json["resourceId"]
    mongoResponse = blogArticleCollection.find_one(
        {"_id" : ObjectId(resourceId)})
    if(isEmpty(mongoResponse)):
        msg="article not found"
        code = 404
        return jsonify(msg), code 
    downvotersId=mongoResponse["downvotersId"]
    upvotersId=mongoResponse["upvotersId"]
    upvotes=mongoResponse["upvotes"]
    downvotes=mongoResponse["downvotes"]
    if userId in downvotersId:
        downvotes=mongoResponse["downvotes"]
        downvotes=int(downvotes)-1
        upvotes=int(upvotes)+1
        upvotersId.append(userId)
        downvotersId.remove(userId)
    elif userId in upvotersId:
        upvotersId.remove(userId)
        upvotes=int(upvotes)-1
    else : 
        upvotersId.append(userId)
        upvotes=int(upvotes)+1
    code=200
    myquery = { "_id": ObjectId(resourceId)}
    newvalues = { "$set": { "upvotes": upvotes,"upvotersId":upvotersId,
    "downvotes":downvotes,"downvotersId":downvotersId } }
    response={"upvotes": upvotes,"upvotersId":upvotersId}
    blogArticleCollection.update_one(myquery, newvalues)
    mongoResponse = blogArticleCollection.find_one(
        {"resourceId" : ObjectId(resourceId)})
    return jsonify(response),code

@blogRecSysAPI.route(blogBase + '/downvoteblog', methods = ['POST'])
def downvoteBlogArticle():
    code = None
    response={}
    userId = request.json["userId"]
    resourceId = request.json["resourceId"]
    mongoResponse = blogArticleCollection.find_one(
        {"_id" : ObjectId(resourceId)})
    if(isEmpty(mongoResponse)):
        code = 404
        msg="article not found"
        return jsonify(msg), code 
    downvotersId=mongoResponse["downvotersId"]
    upvotersId=mongoResponse["upvotersId"]
    upvotes=mongoResponse["upvotes"]
    downvotes=mongoResponse["downvotes"]
    if userId in upvotersId:
        downvotes=int(downvotes)+1
        upvotes=int(upvotes)-1
        upvotersId.remove(userId)
        downvotersId.append(userId)
    elif userId in downvotersId:
        downvotersId.remove(userId)
        downvotes=int(downvotes)-1
    else : 
        downvotersId.append(userId)
        downvotes=int(downvotes)+1
    code=200
    myquery = { "_id": ObjectId(resourceId)}
    newvalues = { "$set": { "upvotes": upvotes,"upvotersId":upvotersId,
    "downvotes":downvotes,"downvotersId":downvotersId } }
    response={"downvotes": downvotes,"downvotersId":downvotersId}
    blogArticleCollection.update_one(myquery, newvalues)
    #mongoResponse = blogArticleCollection.find_one(
    #    {"_id" : ObjectId(resourceId)})
    return jsonify(response),code

@blogRecSysAPI.route(blogBase + '/commentonarticle', methods = ['POST'])
def addCommentToArticle():
    #now = datetime.datetime.now()   #using datetime module
    #using epoch
    seconds=time()
    response={}
    code = None
    #userId = request.json["userId"]
    resourceId = request.json["resourceId"]
    cmnts = request.json["comments"]
    mongoResponse = blogArticleCollection.find_one({"_id" : ObjectId(resourceId)})
    if(isEmpty(mongoResponse)):
        code = 404
        response="article not found"
        return jsonify(response), code 
    else:
        code=200
    comments=mongoResponse["comments"]
    commentsUploadTime=mongoResponse["commentsUploadTime"]
    comments.insert(0,cmnts)
    commentsUploadTime.insert(0,seconds)
    myquery = { "_id": ObjectId(resourceId)}
    newvalues = { "$set": { "comments": comments,"commentsUploadTime":commentsUploadTime } }
    blogArticleCollection.update_one(myquery, newvalues)
    mongoResponse = blogArticleCollection.find_one(
        {"_id" : ObjectId(resourceId)})
    response={"comments": comments,"commentsUploadTime":commentsUploadTime }
    return jsonify(response),code

def getArticlesByTitle(title):
    mongoResponse = list(blogArticleCollection.find({"title" : title}))
    response = list()
    for i in mongoResponse:
        tempDict = dict()
        for key in i:
            tempDict[key] = i[key]
        tempDict['_id'] = str(tempDict['_id'])
        response.append(tempDict)   
    return response

def getArticlesByOwnerName(ownerName):
    mongoResponse = list(blogArticleCollection.find({"ownerName" : ownerName}))
    response = list()
    for i in mongoResponse:
        tempDict = dict()
        for key in i:
            tempDict[key] = i[key]
        tempDict['_id'] = str(tempDict['_id'])
        response.append(tempDict)
    return response

def getArticlesByTags(tags):
    response = []
    response = list()
    mongoResponse = list(blogArticleCollection.find())
    for i in tags:
        for j in mongoResponse:
            if i in j["tags"]:
                tempDict = dict()
                for key in j:
                    tempDict[key] = j[key]
                tempDict['_id'] = str(tempDict['_id'])
                response.append(tempDict)
    return response

def getArticlesByCategory(categoryName):
    mongoResponse = list(blogArticleCollection.find({"category" : categoryName}))
    response = list()
    for i in mongoResponse:
        tempDict = dict()
        for key in i:
            tempDict[key] = i[key]
        response.append(tempDict)
        tempDict['_id'] = str(tempDict['_id'])
    return response

@blogRecSysAPI.route(blogBase + '/searchArticle',methods = ['POST'])
def searchBlogAtricles():
    code = None
    searchString = request.json["searchString"]
    #Search by title
    titleResponse = getArticlesByTitle(searchString)
    #Search by tags
    tagsResponse = getArticlesByTags(searchString.split())
    #Search by ownerName
    ownerNameResponse = getArticlesByOwnerName(searchString)
    #Search by Category
    categoryResponse = getArticlesByCategory(searchString)
    #final Response
    finalResponse = list((titleResponse + ownerNameResponse + categoryResponse + tagsResponse))
    if(len(finalResponse) == 0):
        code = 400
        msg="no articles found"
        return jsonify(msg),code
    else:
        code = 200
    return jsonify(finalResponse),code


@blogRecSysAPI.route(blogBase + '/getAllArticles', methods = ['GET','POST'])
def getAllArticles():
    if request.method=='GET':
        code = None
        mongoResponse = list(blogArticleCollection.find())
        response = list()
        for i in mongoResponse:
            tempDict = dict()
            for key in i:
                tempDict[key] = i[key]
            response.append(tempDict)
            del tempDict['_id']
        if(not len(response)):
            code = 400
        else:
            code = 200
        return jsonify(response), code

    else:
    	msg="Use GET method"
    	return jsonify(msg),405

###################################### Blog API Ending ############################################

###################################### Recommender System Beginning ###############################

@blogRecSysAPI.route(recSysBase + '/getRecommendedArticles', methods = ['GET'])
def recommenderSystem():
    code = None
    response = []
    mongoResponse = blogArticleCollection.find().sort("upvotes", -1)
    response = list()
    for i in mongoResponse:
        tempDict = dict()
        for key in i:
            tempDict[key] = i[key]
        response.append(tempDict)
        tempDict['_id'] = str(tempDict['_id'])
    if(len(response)):
        code = 200
    else:
        code = 400
    return jsonify(response), code

###################################### Recommender System Ending ##################################
