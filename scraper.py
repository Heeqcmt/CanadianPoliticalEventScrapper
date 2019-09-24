import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#Liberal Ontario
#need to add data storing 


url = 'https://ontarioliberal.ca/events/'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all(id='events-listing')

for divTags in eventList:   
    divDesc = divTags.descendants
    for eventWrapper in divDesc:
        if(eventWrapper.name=='p' and eventWrapper.get('class',' ')==['entry-date']):
            print("Date: " + eventWrapper.text)
        elif(eventWrapper.name=='h2'):
            print("Name: "+ eventWrapper.text)
        elif(eventWrapper.name=='p' and eventWrapper.get('class',' ')==['time']):
            print("Time: " + eventWrapper.text)
        elif(eventWrapper.name=='p' and eventWrapper.get('class',' ')==['excerpt']):
            print("Description: " + eventWrapper.text)
        elif(eventWrapper.name=='p' and eventWrapper.get('class',' ')==['type ticketed']):
            print("isTicketed " + eventWrapper.text)
