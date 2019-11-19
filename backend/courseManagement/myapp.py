# Flask main application

from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__, )
app.config.from_pyfile('config.py')
from config import client

from plagiarismCheckViews import plagiarismCheckAPI
from attendanceViews import attendanceAPI
from assignmentViews import assignmentAPI
from materialViews import materialAPI
from managementViews import managementAPI

app.register_blueprint(plagiarismCheckAPI)
app.register_blueprint(attendanceAPI)
app.register_blueprint(assignmentAPI)
app.register_blueprint(materialAPI)
app.register_blueprint(managementAPI)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Origin','127.0.0.1')
  return response


if __name__ == '__main__':
    app.run(port=5001, host="127.0.0.1")