import mysql.connector

mydb = mysql.connector.connect(
    host="mymysql.senecacollege.ca",
    user = "prj666_193a03",
    passwd= "adQZ@8552",
    database="prj666_193a03"   
)
mycursor = mydb.cursor()
mycursor.execute("update OFFICIALEVENT set OFFICIALEVENT.date = TRIM(Replace(Replace(Replace(OFFICIALEVENT.date,'\t',''),'\n',''),'\r','')) WHERE ID > 0;")
mycursor.execute("update OFFICIALEVENT set OFFICIALEVENT.description = TRIM(Replace(Replace(Replace(OFFICIALEVENT.description,'\t',''),'\n',''),'\r','')) WHERE ID > 0;")
mycursor.execute("update OFFICIALEVENT set OFFICIALEVENT.location = TRIM(Replace(Replace(Replace(OFFICIALEVENT.location,'\t',''),'\n',''),'\r','')) WHERE ID > 0;")
mydb.commit()
print("cleaned")
