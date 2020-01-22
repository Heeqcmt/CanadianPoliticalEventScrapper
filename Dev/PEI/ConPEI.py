import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector
#Liberal Ontario
#need to add data storing 

mydb = mysql.connector.connect(
    host="mymysql.senecacollege.ca",
    user = "prj666_193a03",
    passwd= "adQZ@8552",
    database="prj666_193a03"   
)

mycursor = mydb.cursor()
eventDic={}
sqlInsert =  "INSERT INTO OFFICIALEVENT (title,description,address,province,location,date,party,link) VALUES ( %s,%s,%s, %s, %s, %s, %s,%s)"




url = 'http://www.peipc.ca/dsuebee99/calendar'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")