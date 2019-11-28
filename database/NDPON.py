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
sqlInsert = "INSERT INTO OFFICIALEVENT (title,description,province,location,date,party,link) VALUES ( %s,%s, %s, %s, %s, %s,%s)"

url = 'https://www.ontariondp.ca/events'


response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")




response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div','block--event-list--event')
print(eventList)
for event in eventList:
    eventDic["date"]=event.find('div','event-date').text
    eventDic["title"]=event.find('a').text
    eventDic["location"]= event.find('div','event-location').text
    eventDic["link"]=event.find('a','social-tab rsvp-tab')['href']
    print(eventDic)
