from bs4 import BeautifulSoup
import requests
import pymongo
import json


myclient = pymongo.MongoClient("localhost", 27017)
mydb = myclient.people
mycol = mydb.html

links_list = []

url = "http://www.google.co.in"

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data,'html.parser')

for link in soup.find_all('a'):
    links_list.append(link.get('href'))
    # print(link.get('href'))
mycol.insert_one({"links":links_list})
# print(links_list)
