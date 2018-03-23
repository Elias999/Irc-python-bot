#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
from googlesearch import search



def get_kairo(querry):
    for url in search(querry, stop=2):
        #print(url)
        return url

meros='salamina'
querry = "meteo"+ " " + meros
url = get_kairo(querry)

content = urlopen(url).read()

soup = BeautifulSoup(content,"lxml")
#mydivs = soup.find("div", {"class": "perhour rowmargin"})
#print(mydivs)
c = open("new_text.txt","w")
text = soup.get_text()#θελω να βγαινει σε html
c.write(text)
#class = "perhour rowmargin"
