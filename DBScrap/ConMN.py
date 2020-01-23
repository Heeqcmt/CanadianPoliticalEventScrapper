import requests
import urllib.request
import time
from bs4 import BeautifulSoup
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
eventDic={}
sqlInsert =  "INSERT INTO OFFICIALEVENT (title,province,location,date,party,link) VALUES ( %s, %s, %s, %s, %s,%s)"


#connection to event page and parsing html
url = 'https://www.pcmanitoba.com/calendar'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div',class_='content')
        
for event in eventList:
    eventUrl = "https://www.pcmanitoba.com"+event.find("a")["href"]
    eventResp = requests.get(eventUrl)
    eventSoup = BeautifulSoup(eventResp.text,"html.parser")
    eventDic["link"]=eventUrl
    eventDic["title"]=eventSoup.find(id="headline").h2.text
    eventDic["party"] = "Conservative"
    eventDic["province"]="MN"
    eventDetail = eventSoup.find_all(class_="event-detail")
    eventDic["location"]="Please see official site for more information"
    eventDic["date"]="Please see official site for more information"
    
    
    for detail in eventDetail:
        if(detail.h6.text == "WHEN"):  
            eventDic["date"]=detail.div.text
        elif(detail.h6.text == "WHERE"):
            eventDic["location"]=detail.div.text
    
    val = (eventDic["title"],eventDic["province"],eventDic["location"],eventDic["date"],eventDic["party"],eventDic["link"])
    mycursor.execute(sqlInsert,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted")

