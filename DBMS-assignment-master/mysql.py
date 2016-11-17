import MySQLdb

infile = open("TB_burden_countries_2016-08-18.csv","r")
db = MySQLdb.connect("localhost","root","Chiru@123","WHO" )
cursor = db.cursor()

for record in infile:
	print(record)
	cursor.execute("""INSERT INTO tuberculosis VALUES(%s,%s,%s,%s,%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f""",record)
	db.commit()

# disconnect from server
db.close()