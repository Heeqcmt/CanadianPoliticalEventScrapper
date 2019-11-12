import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector
#NDP AB
#need to add data storing 

mydb = mysql.connector.connect(
    host="mymysql.senecacollege.ca",
    user = "prj666_193a03",
    passwd= "adQZ@8552",
    database="prj666_193a03"
    
    
)

mycursor = mydb.cursor()
url = 'https://www.albertandp.ca/events'

response = requests.get(url)
eventDic ={}
soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('section','event-item')
sqlInsert = "INSERT INTO OFFICIALEVENT (title,description,province,location,date,party,link) VALUES ( %s, %s, %s, %s, %s, %s,%s)"

for event in eventList:
    eventDic["title"]=event.find("h1",class_="event-headline").text
    eventDic["date"]=event.find("span",class_="detail-line-inner").text
    location = event.find("li",class_="event-location")
    eventDic["location"]=location.find("span",class_="detail-line-inner").text
    eventDic["description"]=event.find("p").text
    eventDic["link"]="https://www.albertandp.ca"+event.find("a",class_="view-link")["href"]
    eventDic["party"]="NDP"
    eventDic["province"]="AB"
    val = (eventDic["title"],eventDic["description"],eventDic["province"],eventDic["location"], eventDic["date"],eventDic["party"],eventDic["link"])
    mycursor.execute(sqlInsert,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
