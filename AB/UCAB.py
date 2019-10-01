import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#UCP AB
#need to add data storing 

f = open("UCPAB.txt","w+")
url = 'https://www.unitedconservative.ca/'

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

eventList = soup.find_all('div',class_='hidden-md-up d-md-table-cell align-middle g-py-15 g-px-20')
        
for event in eventList:
    f.write("Title: "+event.find('a',class_="g-color-gray-dark-v2").text+"\n")
    f.write("Time: "+event.find('h6',class_="g-color-gray-dark-v5 g-font-style-normal").text+"\n")
    f.write("Location: "+event.find('em',class_="g-color-gray-dark-v5 g-font-style-normal").text+"\n")
    f.write("Link: https://www.unitedconservative.ca"+event.find('a',class_="g-color-gray-dark-v2")["href"]+"\n\n\n\n")
