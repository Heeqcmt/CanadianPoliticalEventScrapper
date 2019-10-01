import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#Con MN
#need to add data storing 

f = open("ConMN.txt","w+")
url = 'https://www.pcmanitoba.com/calendar'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div',class_='content')
        
for event in eventList:
    eventUrl = "https://www.pcmanitoba.com"+event.find("a")["href"]
    eventResp = requests.get(eventUrl)
    eventSoup = BeautifulSoup(eventResp.text,"html.parser")
    print("Link: "+eventUrl+"\n")
    print("Title: "+eventSoup.find(id="headline").h2.text+"\n")

    eventDetail = eventSoup.find_all(class_="event-detail")
    
    for detail in eventDetail:
        if(detail.h6.text == "WHEN"):  
            print("Date: "+detail.div.text+"\n")
        elif(detail.h6.text == "WHERE"):
            print("Location: "+detail.div.text+"\n\n\n\n" )
