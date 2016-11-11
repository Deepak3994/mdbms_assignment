import sys
import pandas as pd 
import pymongo
import json
import os


def import_content(filepath):
	mng_client = pymongo.MongoClient()
	#connecting to the ddatabase
	mng_db = mng_client.TB
	collection_name = 'tb_burden'
	db = mng_db.collection_name
	#reading csv file
	data = pd.read_csv(filepath)
	#converting to json
	data_json = json.loads(data.to_json(orient='records'))
	#inserting to mongodb
	db.insert(data_json)

#main function
if __name__ == '__main__':
	filepath = 'TB_burden_countries_2016-08-18.csv'
import_content(filepath)