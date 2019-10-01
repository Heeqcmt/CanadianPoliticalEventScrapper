import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#NDP MN
#need to add data storing 

f = open("NDPMN.txt","w+")
url = 'https://www.mbndp.ca/events'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div',class_='events-list')
        
for event in eventList:
   f.write("Name: "+event.find("h3").text+"\n")
   f.write("Date: "+event.find("h5").text+"\n")
   f.write("Location: "+event.find("div",class_="event-venue").text+"\n")
   f.write("Description: "+event.find("p").text +"\n\n\n")
