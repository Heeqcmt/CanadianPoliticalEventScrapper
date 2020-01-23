import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector
#ConservativesOntario
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
eventDic={}
sqlInsert =  "INSERT INTO OFFICIALEVENT (title,province,location,date,party,link) VALUES ( %s, %s, %s, %s, %s,%s)"



url = 'https://www.ontariopc.ca/events'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div','event')
        
for event in eventList:
    tagList = event.descendants
    for tag in tagList:
        if(tag.name == 'h4'):
            eventDic["title"] = tag.text
        elif(tag.name == 'a' and not tag.has_attr('class')):
            eventDic["location"]=tag.text
        elif(tag.name == 'p'):
            eventDic["date"]= tag.text 
        elif(tag.name == 'a' and tag.has_attr('class')):
            eventDic["link"]=  "https://www.ontariopc.ca/" + tag['href'] 
    val = (eventDic["title"],"ON",eventDic["location"],eventDic["date"],"Conservative",eventDic["link"])
    mycursor.execute(sqlInsert,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted")


      
