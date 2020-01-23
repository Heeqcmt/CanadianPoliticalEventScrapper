import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import mysql.connector
#librals BC
#need to add data storing 
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
      

      
