from bs4 import BeautifulSoup
import requests

url = 'http://www.imdb.com/ls000183546'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

movie_list = soup.findAll('div', {'class': "lister-item mode-detail"})

for titles in movie_list