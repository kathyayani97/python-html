from bs4 import BeautifulSoup
import requests
import pymongo
import json


myclient = pymongo.MongoClient("localhost", 27017)
mydb = myclient.people
mycol = mydb.html



url = "http://www.google.com/"

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data,'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
    #mycol.insert_one(link)

