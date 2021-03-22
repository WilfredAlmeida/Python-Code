import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",passwd="",database="capstone")

c=db.cursor()

#c.execute("insert into sample (pname,page) values ('A',12)") 
	#inserts values specified

sq="insert into sample (pname,page) VALUES (%s,%s)"
l=(['b',1],['c',2],['d',4])
c.executemany(sq,l)
"""executemany() allows to execute a single query for multiple values. 
IMP: for executing query with only one dynamic value use execute() method."""


c.execute("select * from sample")

r=c.fetchall()

for i in r:
	print(i[0]," ",i[1])