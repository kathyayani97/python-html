from bs4 import BeautifulSoup
import requests
import pymongo

myclient = pymongo.MongoClient("localhost", 27017)
mydb = myclient.people
mycol = mydb.scrappy

url = 'http://www.imdb.com/list/ls000183546'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


movie_list = soup.findAll('div', {'class':"lister-item-content"})

imdb = []
for movie in movie_list:

    director_actor_list = movie.findAll('p',{"class": "text-muted text-small"})[1].findAll('a', href = True)


    actors = {}

    for stars in director_actor_list[1:] :

        actors[stars.contents[0]] = stars.get('href')

    imdb.append({"title":movie.find('h3',{"class":"lister-item-header"}).find('a').contents[0],
        "runtime":movie.find('p',{"class":"text-muted text-small"}).find('span',{"class":"runtime"}).contents[0],
        "director":{director_actor_list[0].contents[0] : director_actor_list[0].get('href')},
        "actor": actors})
print(imdb)

mycol.insert_one(actors)