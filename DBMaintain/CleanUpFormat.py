import mysql.connector
import DBInfo.Information as DB



mydb = mysql.connector.connect(
    host = DB.host,
    user = DB.user,
    passwd= DB.passwd,
    database=DB.database
    
    
)
mycursor = mydb.cursor()
mycursor.execute("update OFFICIALEVENT set OFFICIALEVENT.date = TRIM(Replace(Replace(Replace(OFFICIALEVENT.date,'\t',''),'\n',''),'\r','')) WHERE ID > 0;")
mycursor.execute("update OFFICIALEVENT set OFFICIALEVENT.description = TRIM(Replace(Replace(Replace(OFFICIALEVENT.description,'\t',''),'\n',''),'\r','')) WHERE ID > 0;")
mycursor.execute("update OFFICIALEVENT set OFFICIALEVENT.location = TRIM(Replace(Replace(Replace(OFFICIALEVENT.location,'\t',''),'\n',''),'\r','')) WHERE ID > 0;")
mydb.commit()
print("cleaned")
