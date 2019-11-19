import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#NDP ON
#need to add data storing 


url = 'https://www.ontariondp.ca/events'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div','block--event-list--event')

for event in eventList:
    f.write("Date: "+ event.find('div','event-date').text+"\n")
    f.write("Title: "+ event.find('a').text+"\n")      
    f.write("Location: "+ event.find('div','event-location').text+"\n") 
    f.write("RSVP: "+ event.find('a','social-tab rsvp-tab')['href']+"\n")
