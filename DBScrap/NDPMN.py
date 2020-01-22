import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector

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
sqlInsert = "INSERT INTO OFFICIALEVENT (title,description,province,location,date,party,link) VALUES ( %s,%s, %s, %s, %s, %s,%s)"

url = 'https://www.mbndp.ca/events'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")


eventList = soup.find_all('ul',"event-wrap")

        
for event in eventList:
    eventDic["title"] = event.find("h3").text
    eventDic["date"] = event.find("h5").text
    eventDic["location"] = event.find("div", class_="event-venue").text
    eventDic["description"] = event.find("p").text
    eventDic["province"] = "MN"
    eventDic["party"] = "NDP"
    eventDic["link"] = "https://www.mbndp.ca" + \
    event.find("a", "submit-button")["href"]
    val = (eventDic["title"], eventDic["description"], eventDic["province"],eventDic["location"], eventDic["date"], eventDic["party"], eventDic["link"])
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

      
