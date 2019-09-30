import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#NDP BC
#need to add data storing 

f = open("NDPBC.txt","w+")
url = 'https://www.bcndp.ca/events'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div','event')
        
for event in eventList:
    f.write("Date: "+ event.find('div',class_='date').text+"\n")
    f.write("Name: "+event.find('a').text +"\n")
    f.write("Link: "+ event.find('a')['href']+"\n")
    f.write("Description: "+ event.find('div',class_='desc').text+"\n\n\n\n\n\n")
      

      