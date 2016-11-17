import csv
infile = open("types.csv","r")
outfile = open("create_table.text","w")
count = 0 
header = []
types = []
for record in infile:
	if count == 0:
		record_split = record.split(",")
		for x in range(len(record_split)-1):
			header.append(record_split[x])
		count +=1
	else:
		record_split = record.split(",")
		for x in range(len(record_split)-1):
			types.append(record_split[x])
		count +=1
outfile.write("create table tuberculosis(")
for x in range(len(header)):
	message = header[x]+" "+types[x]+","+"\n"
	outfile.write(message)
outfile.write(");")
