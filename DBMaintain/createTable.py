import mysql.connector
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import DBInfo.Information as DB



mydb = mysql.connector.connect(
    host = DB.host,
    user = DB.user,
    passwd= DB.passwd,
    database=DB.database
    
    
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE OFFICIALEVENT")
mycursor.execute("CREATE TABLE OFFICIALEVENT (id INT AUTO_INCREMENT PRIMARY KEY, title TEXT ,description TEXT,address TEXT, province TEXT,location TEXT,date TEXT,party TEXT,link TEXT)")
mydb.commit()
print("table dropped and created")