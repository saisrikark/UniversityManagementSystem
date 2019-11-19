#!/usr/bin/env python
import sys
import pandas as pd
import pymongo
import json
import os



def import_content(filepath,collection_name):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['mydb']  #So here the database name is 'mydb' could be changed accordingly as per the project is concerned.
    #collection_name = 'student' 
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
  filepath = '/home/sachu/Desktop/test1.csv'
  col_name=raw_input('Enter collection name: ')  
  import_content(filepath,col_name)
