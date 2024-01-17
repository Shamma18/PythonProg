# import pywhatkit as pyw
# a='+917888799391'
# pyw.sendwhatmsg(a,'hello',11,5)



# import requests
# city=input ('city name')
# print(city)
# print('report')
# url='https://wttr.in/{}'.format(city)
# res=requests.get(url)
# print(res.text)




# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root')
# if con.is_connected():
#     print("connected")
# else:
#     print('not connected')

# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root')
# cur=con.cursor()
# cur.execute("create database data1")

# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root',database='data1')
# cur=con.cursor()
# st="create table msg(phone varchar(200),m varchar(200),hour varchar(200),minutes varchar(200))"
# cur.execute(st)


# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root',database='data1')
# cur=con.cursor()
# st="insert into msg values('+917888799391','hello','10','45')"
# cur.execute(st)
# con.commit()

# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root',database='data1')
# cur=con.cursor()
# st="insert into msg values('+917888799391','hello','10','46')"
# cur.execute(st)
# con.commit()

# import mysql.connector
# con=mysql.connector.connect(host='localhost',password='Admin@123',user='root',database='data1')
# cur=con.cursor()
# st="insert into msg values('+917888799391','hello','10','47')"
# cur.execute(st)
# con.commit()


import mysql.connector
con=mysql.connector.connect(host='localhost',password='Admin@123',user='root',database='data1')
cur=con.cursor()
st="select * from msg"
cur.execute(st)
result=cur.fetchall()
for rec in result:

    a=str(rec[0])
    b=str(rec[1])
    c=int(rec[2])
    
    d=int(rec[3])
    import pywhatkit as pyw
    pyw.sendwhatmsg(str(a),str(b),c,d)

con.commit()