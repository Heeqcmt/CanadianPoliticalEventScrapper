import mysql.connector

mydb = mysql.connector.connect(
    host="mymysql.senecacollege.ca",
    user = "prj666_193a03",
    passwd= "adQZ@8552",
    database="prj666_193a03"   
)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE OFFICIALEVENT")
mycursor.execute("CREATE TABLE OFFICIALEVENT (id INT AUTO_INCREMENT PRIMARY KEY, title TEXT ,description TEXT,address TEXT, province TEXT,location TEXT,date TEXT,party TEXT,link TEXT)")
mydb.commit()
print("table dropped")