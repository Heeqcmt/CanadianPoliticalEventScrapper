import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector

#NDP MN
#need to add data storing 
mydb = mysql.connector.connect(
    host="mymysql.senecacollege.ca",
    user = "prj666_193a03",
    passwd= "adQZ@8552",
    database="prj666_193a03"   
)
mycursor = mydb.cursor()
eventDic={}
sqlInsert = "INSERT INTO OFFICIALEVENT (title,province,location,date,party,link) VALUES ( %s, %s, %s, %s, %s,%s)"


#debug
f = open("ConMN.txt","w+")

url = 'https://www.mbndp.ca/events'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventwrap = soup.find_all('ul',class_='event-wrap')
eventList = eventwrap.find_all('li')
        
for event in eventList:
   #eventDic["title"]=event.find("h3").text
   #eventDic["date"]=event.find("h5").text
   #eventDic["location"]=event.find("div",class_="event-venue").text
   #eventDic["description"]=event.find("p").text 
   f.write(event.find("a",class_="submit-button")["href"])
   #eventDic["province"]="MN"
   #eventDic["party"]="NDP"
   
