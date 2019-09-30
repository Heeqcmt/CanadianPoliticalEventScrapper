import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#ConservativesOntario
#need to add data storing 

f = open("ConON.txt","w+")
url = 'https://www.ontariopc.ca/events'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div','event')
        
for event in eventList:
    tagList = event.descendants
    for tag in tagList:
        if(tag.name == 'h4'):
            f.write("name: "+tag.text+"\n")
        elif(tag.name == 'a' and not tag.has_attr('class')):
            f.write("Location: "+tag.text+"\n")
        elif(tag.name == 'p'):
            f.write("Time: " + tag.text +"\n")
        elif(tag.name == 'a' and tag.has_attr('class')):
            f.write("Registration: https://www.ontariopc.ca/" + tag['href'] + "\n\n\n\n")

      
