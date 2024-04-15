import requests
from bs4 import BeautifulSoup

# URL de la page Wikipedia sur la chimie
url = "https://fr.wikipedia.org/wiki/Chimie"

# Faire une requête pour obtenir le contenu de la page
response = requests.get(url)
content = response.content

# Utiliser BeautifulSoup pour analyser le contenu HTML de la page
#soup = BeautifulSoup(content, 'html.parser')

soup = BeautifulSoup (content,'html.parser')
img = soup.find('img')
print(img)

