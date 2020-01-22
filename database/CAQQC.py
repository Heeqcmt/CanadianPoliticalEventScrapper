import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector
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

url = 'https://coalitionavenirquebec.org/fr/activites'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

aTags = soup.find_all('a')

for tag in aTags:
    if(tag.h3):
        eventURL = tag['href']
        eventResp = requests.get(eventURL)
        eventSoup = BeautifulSoup(eventResp.text,"html.parser")
        eventDic["link"]=eventURL
        eventDic["title"]=eventSoup.h1.text
        data = eventSoup.find_all('span')
        for span in data:
            if(span.i):
                if(span.i["class"]==['fa','fa-calendar']):
                    eventDic["date"]=span.text
                elif(span.i["class"]==['fa','fa-clock-o']):
                    eventDic["date"] = eventDic["date"]+span.text
        eventDic["desc"]=eventSoup.find("div","col-lg-12 wysiwyg-container").text
        address = eventSoup.find('h3',class_="w-subtitle spacing--medium",text="Adresse")  
        addParent = address.parent
        eventDic["location"]=addParent.strong.text
        val = (eventDic["title"],"QC",eventDic["location"],eventDic["date"],"CAQ",eventDic["link"])
        mycursor.execute(sqlInsert,val)
        mydb.commit()
        print(mycursor.rowcount,"record inserted")
                
        
