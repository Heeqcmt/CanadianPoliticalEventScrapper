import requests
from urllib.request import Request,urlopen
import time
from bs4 import BeautifulSoup
import mysql.connector
#ConservativesOntario
#need to add data storing 


mydb = mysql.connector.connect(
    host="mymysql.senecacollege.ca",
    user = "prj666_193a03",
    passwd= "adQZ@8552",
    database="prj666_193a03"   
)

mycursor = mydb.cursor()
eventDic={}
sqlInsert =  "INSERT INTO OFFICIALEVENT (title,address,province,location,date,party,link) VALUES ( %s,%s, %s, %s, %s, %s,%s)"



url = 'https://nbliberal.ca/events/'
header = {'User-Agent':'Mozilla/5.0'}
response = Request(url,headers=header)
page = urlopen(response)
soup = BeautifulSoup(page,features="html.parser")



eventTable = soup.find("table","events-table")
linkList = eventTable.find_all("td")

for links in linkList:
    if(links.find("a")):
        link = links.find("a")["href"]
        eventDic["link"] = link
        #get into the eventpage
       
        header = {'User-Agent':'Mozilla/5.0'}
        response = Request(link,headers=header)
        page = urlopen(response)
        soup = BeautifulSoup(page,features="html.parser")

        #get details
        # print(soup.find("h4","event-date").text)
        # print(soup.find("h2","post-headline").text)
        # print(soup.find("p","event-venue").text)
        # print(soup.find("p","event-address").text+" "+soup.find("p","event-town").text) 
        eventDic["date"]=soup.find("h4","event-date").text
        eventDic["title"] = soup.find("h2","post-headline").text
        eventDic["location"] = (soup.find("p","event-venue").text)
        eventDic["address"]=(soup.find("p","event-address").text+" "+soup.find("p","event-town").text)
        val = (eventDic["title"],eventDic["address"],"NB",eventDic["location"],eventDic["date"],"Liberal",eventDic["link"])
        mycursor.execute(sqlInsert,val)
        mydb.commit()
        print(mycursor.rowcount,"record inserted")





    

    



      
