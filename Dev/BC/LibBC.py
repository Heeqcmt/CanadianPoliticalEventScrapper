import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import mysql.connector
#librals BC
#need to add data storing 

mydb = mysql.connector.connect(
    host="mymysql.senecacollege.ca",
    user = "prj666_193a03",
    passwd= "adQZ@8552",
    database="prj666_193a03"
    
    
)
mycursor = mydb.cursor()
eventDic = {}
url = 'https://secure.bcliberals.com/event'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div','event')
sqlInsert = "INSERT INTO OFFICIALEVENT (title,description,province,date,party,link) VALUES (%s, %s, %s,%s, %s, %s)"
        
for event in eventList:
    eventDic["date"]=event.find('div',class_='date').text
    eventDic["title"]=event.find('a').text
    eventDic["link"]=event.find('a')['href']
    eventDic["description"]=event.find('div',class_='desc').text
    val = (eventDic["title"],eventDic["description"],"BC",eventDic["date"],"Liberal",eventDic["link"])
    mycursor.execute(sqlInsert,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
      

      
