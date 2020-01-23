import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector
#Liberal Ontario
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
sqlInsert =  "INSERT INTO OFFICIALEVENT (title,description,address,province,location,date,party,link) VALUES ( %s,%s,%s, %s, %s, %s, %s,%s)"




url = 'https://ontarioliberal.ca/events/'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all("div","cell large-4 medium-6 events-listing-single")

for events in eventList:
    detailLink = events.find("a")["href"]
    detailReponse = requests.get(detailLink)
    newSoup = BeautifulSoup(detailReponse.text,"html.parser")
    address = newSoup.find("p","location")
    location = address.span.extract()
    eventDic["link"]=(events.find("a")["href"])
    eventDic["date"]=(events.find("p","entry-date").text+" "+events.find("p","time").text)
    eventDic["title"]=(events.find("h2").text)
    eventDic["desc"]=(events.find("p","excerpt").text)
    eventDic['location']=location.text
    eventDic["address"] = address.text
    val = (eventDic["title"],eventDic["desc"],eventDic["address"],"ON",eventDic["location"],eventDic["date"],"Liberal",eventDic["link"])
    mycursor.execute(sqlInsert,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted")
    


    
            
