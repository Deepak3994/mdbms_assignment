import csv
import json
import pymongo
from pymongo import MongoClient


class mongo:
	def __init__(self):
		self.infile = open("TB_burden_countries_2016-08-18.csv","r")
		self.outfile = open("jsonfile.json","w")
		self.__connect_database()
		self.__csvtojson()
		self.__LoadtoMongo()

	def __connect_database(self):
		connection=MongoClient()
		self.db=connection.WHO
		self.collection=self.db.Tuberculosis

	def __csvtojson(self):
		fieldnames = ("country","iso2","iso3","iso_numeric","g_whoregion","year","e_pop_num","e_prev_100k","e_prev_100k_lo","e_prev_100k_hi","e_prev_num","e_prev_num_lo","e_prev_num_hi","source_prev",
		"e_mort_exc_tbhiv_100k","e_mort_exc_tbhiv_100k_lo","e_mort_exc_tbhiv_100k_hi","e_mort_exc_tbhiv_num","e_mort_exc_tbhiv_num_lo","e_mort_exc_tbhiv_num_hi","e_mort_tbhiv_100k","e_mort_tbhiv_100k_lo",
		"e_mort_tbhiv_100k_hi","e_mort_tbhiv_num","e_mort_tbhiv_num_lo","e_mort_tbhiv_num_hi","source_mort","e_inc_100k","e_inc_100k_lo","e_inc_100k_hi","e_inc_num","e_inc_num_lo","e_inc_num_hi","source_inc",
		"e_tbhiv_prct","e_tbhiv_prct_lo","e_tbhiv_prct_hi","e_inc_tbhiv_100k","e_inc_tbhiv_100k_lo","e_inc_tbhiv_100k_hi","e_inc_tbhiv_num","e_inc_tbhiv_num_lo","e_inc_tbhiv_num_hi","source_tbhiv",
		"c_newinc_100k","c_cdr","c_cdr_lo","c_cdr_hi")
		reader = csv.DictReader( self.infile, fieldnames)
		out = json.dumps( [ row for row in reader ] )
		self.outfile.write(out)
		self.outfile.close();

	def __LoadtoMongo(self):
		jsonfile=open("jsonfile.json",'r')
		jsonarray=json.loads(jsonfile.read())
		for document in jsonarray:
		   self.collection.insert(document) 

db1 = mongo()