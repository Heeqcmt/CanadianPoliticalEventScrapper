import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
#NDP MN
#need to add data storing 
import DBInfo.Information as DB



mydb = mysql.connector.connect(
    host = DB.host,
    user = DB.user,
    passwd= DB.passwd,
    database=DB.database
    
    
)
mycursor = mydb.cursor()
eventDic={}
sqlInsert = "INSERT INTO OFFICIALEVENT (title,province,location,party,link) VALUES ( %s,%s, %s, %s, %s)"

url = 'https://www.ontariondp.ca/events'


response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")




response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div','block--event-list--event')

for event in eventList:
    eventDic["date"]=event.find('div','event-date').text
    eventDic["title"]=event.find('a').text
    eventDic["location"]= event.find('div','event-location').text
    eventDic["link"]=event.find('a','social-tab rsvp-tab')['href']
    val = (eventDic["title"],"ON",eventDic["location"], "NDP", eventDic["link"])
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
