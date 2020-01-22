import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import mysql.connector
#NDP BC
#need to add data storing 


mydb = mysql.connector.connect(
    host="mymysql.senecacollege.ca",
    user = "prj666_193a03",
    passwd= "adQZ@8552",
    database="prj666_193a03"
    
    
)

mycursor = mydb.cursor()

url = 'https://www.bcndp.ca/events?action_handler=block--campaign-events-search&action=block--campaign-events-search--search-all&json=1'

response = requests.get(url)

data = response.json()

numOfEvent = len(data["markers"])

eventDic ={}

sqlInsert = "INSERT INTO OFFICIALEVENT (title,description,address,province,location,date,party,link) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"

for i in range(numOfEvent):
    eventDic["title"]=data["markers"][i]["title"]
    eventDic["date"]=data["markers"][i]["date"]
    eventDic["location"]=data["markers"][i]["location"]
    eventDic["address"]=data["markers"][i]["address"]
    eventDic["postal Code"]=data["markers"][i]["postal_code"]
    eventDic["description"]=data["markers"][i]["description"]
    eventDic["link"]=data["markers"][i]["link"]
    eventDic["party"]="NDP"
    eventJson = json.dumps(eventDic)
    val = (eventDic["title"],eventDic["description"],eventDic["address"],"BC",eventDic["location"], eventDic["date"],"NDP",eventDic["link"])
    mycursor.execute(sqlInsert,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

      
