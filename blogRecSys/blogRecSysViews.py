from flask import render_template, request, jsonify, Blueprint

blogRecSysAPI = Blueprint('blogRecSysAPI', __name__)

from myapp import app, client
from random import randint, seed
from time import time

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
    ownerId = request.json["ownerId"]
    ownerName = request.json["ownerName"]
    category = request.json["category"]
    info = request.json["info"]
    #token = request.json["token"]
    ##Authorization functionality
    ##Check if user is logged in 
    '''Insert here'''
    ##End here
    #Generate Different Random Number Every Time
    code = None
    seed()
    resourceId = randint(99999,1000000)
    comments = []
    commentsUploadTime = []
    timeUploaded = time()
    upvotes = 0
    upvotersId = []
    downvotes = []
    downvotersId = []
    if(len(tags) == 0):
        tags.add("generic")
    blogArticleCollection.insert_one({
        "title" : title, "tags" : tags,
        "resourceId" : resourceId,
        "ownerId" : ownerId, "ownerName" : ownerName,
        "category" : category, "info" : info,
        "comments" : comments, "commentsUploadTime" : commentsUploadTime,
        "timeUploaded" : timeUploaded,
        "upvotes" : upvotes, "upvotersId" : upvotersId,
        "downvotes" : downvotes, "downvotersId" : downvotersId
    })
    response = {"resourceId" : resourceId}
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
        {"resourceId" : resourceId})
    if(isEmpty(mongoResponse)):
        code = 404
        response = {"res" : "Not Found"}
    else:
        code = 200
        blogArticleCollection.delete_one({"resourceId" : resourceId})
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
    else:
        code = 200
    return jsonify(response), code


@blogRecSysAPI.route(blogBase, methods = ['POST'])
def upvoteBlogArticle():
    pass

@blogRecSysAPI.route(blogBase, methods = [])
def downvoteBlogArticle():
    pass

@blogRecSysAPI.route(blogBase, methods = [])
def addCommentToArticle():
    pass

@blogRecSysAPI.route(blogBase, methods = [])
def searchBlogAtricles():
    pass


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
        del tempDict['_id']
    if(len(response)):
        code = 200
    else:
        code = 400
    return jsonify(response), code

###################################### Recommender System Ending ##################################