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
sqlInsert =  "INSERT INTO OFFICIALEVENT (title,description,province,location,date,party,link) VALUES ( %s,%s, %s, %s, %s, %s,%s)"

url = "https://www.pcnl.ca/events"
respond = requests.get(url)
soup = BeautifulSoup(respond.text,"html.parser")

eventTitle = soup.find("div","crm-container")



if(eventTitle.find("a") == True ):
    link = eventTitle.find("a")["href"]
    eventDic["link"]=link
    eventDic["title"]=eventTitle.find("a").text
    eventDetailRespond = requests.get(link)
    eventSoup = BeautifulSoup(eventDetailRespond.text,"html.parser")
    eventDic["desc"]= eventSoup.find("div","crm-section event_description-section summary").text
    date = eventSoup.find("div","crm-section event_date_time-section")
    eventDic["date"] = (date.find("abbr","dtstart").text
        + " - "+ date.find("abbr","dtend").text)
    eventDic["location"] = (eventSoup.find("div","crm-section event_address-section").text)
    val = (eventDic["title"],eventDic["desc"],"NL",eventDic["location"],eventDic["date"],"Conservative",eventDic["link"])
    mycursor.execute(sqlInsert,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted")
else: 
    print("ConNL no event")
