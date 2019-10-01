import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#NDP BC
#need to add data storing 

f = open("NDPBC.txt","w+")
url = 'https://www.bcndp.ca/events?action_handler=block--campaign-events-search&action=block--campaign-events-search--search-all&json=1'

response = requests.get(url)

data = response.json()

numOfEvent = len(data["markers"])

for i in range(numOfEvent):
    f.write("Title: "+data["markers"][i]["title"]+"\n")
    f.write("Date: "+data["markers"][i]["date"]+"\n")
    f.write("Location: "+data["markers"][i]["location"]+"\n")
    f.write("Address: "+data["markers"][i]["address"]+"\n")
    f.write("Postal Code: "+data["markers"][i]["postal_code"]+"\n")
    f.write("Description: "+data["markers"][i]["description"]+"\n")
    f.write("Link: "+data["markers"][i]["link"]+"\n\n\n")
    

      
