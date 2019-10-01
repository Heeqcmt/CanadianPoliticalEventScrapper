import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#Con MN
#need to add data storing 
#possible fix for format is here

f = open("CAQQC.txt","w+")
url = 'https://coalitionavenirquebec.org/fr/activites'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

aTags = soup.find_all('a')

for tag in aTags:
    if(tag.h3):
        eventURL = tag['href']
        eventResp = requests.get(eventURL)
        eventSoup = BeautifulSoup(eventResp.text,"html.parser")
        f.write("Link: "+ eventURL+"\n")
        f.write("Title: "+ eventSoup.h1.text+"\n")
        data = eventSoup.find_all('span')
        for span in data:
            if(span.i):
                if(span.i["class"]==['fa','fa-calendar']):
                    f.write("Date: "+span.text+"\n")
                elif(span.i["class"]==['fa','fa-clock-o']):
                    f.write("Time: "+span.text+"\n")

        address = eventSoup.find('h3',class_="w-subtitle spacing--medium",text="Adresse")  
        addParent = address.parent
        f.write("location: "+addParent.strong.text+"\n")            
                
        
