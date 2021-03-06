import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector


mydb = mysql.connector.connect(
    host="mymysql.senecacollege.ca",
    user = "prj666_193a03",
    passwd= "adQZ@8552",
    database="prj666_193a03"   
)

mycursor = mydb.cursor()
eventDic={}
sqlInsert =  "INSERT INTO OFFICIALEVENT (title,description,province,date,party,link) VALUES (%s, %s, %s, %s, %s,%s)"

urlList = "https://www.saskparty.com/events?page=1"
response = requests.get(urlList)
firstSoup = BeautifulSoup(response.text,"html.parser")

for link in firstSoup.find_all("a","card event"):
    eventDic["link"] = ("https://www.saskparty.com"+link["href"])
    #get detail by going into new page
    detailRes = requests.get(eventDic["link"])
    detailSoup = BeautifulSoup(detailRes.text,"html.parser")
    eventDic["title"]=detailSoup.find("h2").text
    eventDic["desc"]=detailSoup.find("div","intro").text
    eventDic["date"]=detailSoup.find("div","subtext").text
    val = (eventDic["title"],eventDic["desc"],"SK",eventDic["date"],"Saskatchewan Party",eventDic["link"])
    mycursor.execute(sqlInsert,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted")


    