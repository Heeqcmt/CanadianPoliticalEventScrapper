import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#NDP AB
#need to add data storing 

f = open("NDPAB.txt","w+")
url = 'https://www.albertandp.ca/events'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('section','event-item')
        
for event in eventList:
    f.write("Title: "+event.find("h1",class_="event-headline").text+"\n")
    f.write("Time: "+event.find("span",class_="detail-line-inner").text+"\n")
    location = event.find("li",class_="event-location")
    f.write("Location: "+location.find("span",class_="detail-line-inner").text+"\n")
    f.write("Description: "+event.find("p").text)
    f.write("Link: "+"https://www.albertandp.ca"+event.find("a",class_="view-link")["href"]+"\n\n\n\n")
      