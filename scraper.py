import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#Liberal Ontario
#need to add data storing 

f = open("ontarioLiberalTest.txt","w+")

url = 'https://ontarioliberal.ca/events/'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all(id='events-listing')

for divTags in eventList:   
    divDesc = divTags.descendants
    for eventWrapper in divDesc:
        if(eventWrapper.name=='p' and eventWrapper.get('class',' ')==['entry-date']):
            f.write("Date: " + eventWrapper.text+"\n")
        elif(eventWrapper.name=='h2'):
            f.write("Name: "+ eventWrapper.text+"\n")
        elif(eventWrapper.name=='p' and eventWrapper.get('class',' ')==['time']):
            f.write("Time: " + eventWrapper.text+"\n")
        elif(eventWrapper.name=='p' and eventWrapper.get('class',' ')==['excerpt']):
            f.write("Description: " + eventWrapper.text+"\n\n\n\n")
        #elif(eventWrapper.name=='p' and eventWrapper.get('class',' ')==['type ticketed']):
            #f.write("isTicketed " + eventWrapper.text+"\n")
        elif(eventWrapper.name=='a' ):
            addressURL = eventWrapper['href']
            f.write(eventWrapper['href']+"\n")
            
            
            newResponse = requests.get(addressURL)
            newSoup = BeautifulSoup(newResponse.text,"html.parser")
            descendants = newSoup.descendants
            for tags in descendants:
                if(tags.name=='p' and tags.get('class',' ')==['location']):
                    f.write(tags.text+"\n")
            
