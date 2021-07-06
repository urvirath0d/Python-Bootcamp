import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="!123456!",
  database="employee_mangement"
)

mycursor = mydb.cursor()
print(mydb)

dbse = mydb.cursor()

# dbse.execute("CREATE DATABASE Employee_Mangement")

dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
    print(entry)
    dbse = mydb.cursor()

dbse.execute("CREATE TABLE Employee (emp_id INT , EMP_NAME VARCHAR(255),EMP_SALARY DOUBLE )")
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")

for value in dbse:
    print(value)
    dbse = mydb.cursor()

sql = "INSERT INTO employee (emp_id , EMP_NAME , EMP_SALARY) VALUES (%s,%s,%s)"
val = [
  ('1','A','10000'),
    ('2','B','1000.0'),
    ('3','C','800.0'),
    ('4','D','8000.0'),
    ('5','E','8900.0'),
    ('6','F','5000.0'),
    ('7','G','5600.0'),
    ('8','H','7000.0'),
    ('9','I','6000.0'),
    ('10','J','1500.0'),
    ('11','K','5050.0'),
    ('12','L','4050.0'),
    ('13','M','2500.0'),
    ('14','N','205.0'),
    ('15','0','10060.0')
]

#
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="!123456!",
  database="employee_mangement"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) from employee")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


#
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="!123456!",
  database="employee_mangement"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * from employee WHERE EMP_NAME LIKE('ANU%')")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)