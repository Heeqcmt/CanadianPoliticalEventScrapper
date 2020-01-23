import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector
#UCP AB
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

url = 'https://www.unitedconservative.ca/'

eventDic={}
sqlInsert = "INSERT INTO OFFICIALEVENT (title,province,location,date,party,link) VALUES ( %s, %s, %s, %s, %s,%s)"


response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
eventList = soup.find_all('div',class_='hidden-md-up d-md-table-cell align-middle g-py-15 g-px-20')      
for event in eventList:
    eventDic["title"]=event.find('a',class_="g-color-gray-dark-v2").text
    eventDic["date"]=event.find('h6',class_="g-color-gray-dark-v5 g-font-style-normal").text
    eventDic["location"]=event.find('em',class_="g-color-gray-dark-v5 g-font-style-normal").text
    eventDic["link"]= "https://www.unitedconservative.ca"+event.find('a',class_="g-color-gray-dark-v2")["href"]
    eventDic["province"]="AB"
    eventDic["party"]="United Conservative Party"
    val = (eventDic["title"],eventDic["province"],eventDic["location"], eventDic["date"],eventDic["party"],eventDic["link"])
    mycursor.execute(sqlInsert,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    