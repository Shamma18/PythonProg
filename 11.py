# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root')
# if con.is_connected():
#     print("connected")
# else:
#     print('not connected')

# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root')
# cur=con.cursor()
# cur.execute("create database data")

# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root',database='data')
# cur=con.cursor()
# st="create table emp(id integer(4),name varchar(200),job varchar(200))"
# cur.execute(st)

# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root',database='data')
# cur=con.cursor()
# st="insert into emp values(101,'king','president')"
# cur.execute(st)
# con.commit()

# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root',database='data')
# cur=con.cursor()
# st="select * from emp"
# cur.execute(st)
# result=cur.fetchall()
# for rec in result:
#     print(rec)
# con.commit()

# import qrcode as qr
# img=qr.make("https://www.instagram.com/shamma.garg_/")
# img.save("tcl.png")

import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number='+917888799391'
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)

  
# Validating a phone number 
valid = phonenumbers.is_valid_number(phone) 
  
# Checking possibility of a number 
possible = phonenumbers.is_possible_number(phone) 
  
# Printing the output 
print(valid) 
print(possible) 