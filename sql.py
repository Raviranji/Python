# Python implementation to create a Database in MySQL
import mysql.connector

# connecting to the mysql server
db = mysql.connector.connect(
	host="localhost",
    port='3306',
	user="root",
	passwd="Ranjith219211",
    database='db1'
)

# cursor object c
c = db.cursor()
print ("Server Conneted")

'''
c.execute("""
CREATE TABLE product(
    id INT AUTO_INCREMENT,
    product_name VARCHAR(255),
    product_desc VARCHAR(500),    
    product_price VARCHAR(255),
    PRIMARY KEY (id)
);

""")
print ("Table Created")
'''

'''
result=[('a','abc','$30'),('b','xyz','$60'),('c','abb','$80'),('d','acc','$120'),('e','agg','$130'),('f','aytc','$60'),('g','auii','$90'),('h','iopk','$100'),('i','abcrerer','$30')]
for i,j,l in result:
    print (i,j,l)
    Sinert="Insert into product(product_name,product_desc,product_price)values('%s','%s','%s')"%(i,j,l)   
    c.execute(Sinert)
    db.commit()
    print ("============>Inserted")
'''

'''
productname='Hamam'
productprice='$1000'
rollid=3
supdate ="update product set product_name='%s',product_price='%s' where id='%s'"%(productname,productprice,rollid)
c.execute(supdate)
db.commit()
print("Updated")
'''

'''
rollid=9 
dquery="delete from product where id='%s'"%(rollid)
c.execute(dquery)
db.commit()
print ("Record Deleted")
'''
'''
dquery="TRUNCATE TABLE product;"
c.execute(dquery)
print ("Table Truncated")
'''
'''
dquery="Drop TABLE product;"
c.execute(dquery)
print ("Table Droped")
'''

db.close()
