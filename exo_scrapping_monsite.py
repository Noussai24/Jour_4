import requests
from bs4 import BeautifulSoup

# URL du site à scraper
url = "https://www.fossil.com/fr-fr/montres/montres-pour-femme/meilleures-ventes/"

# Effectuer une requête HTTP GET vers l'URL
response = requests.get(url)
# print (response)
content = response.content
# print (content)

# Créer un objet BeautifulSoup pour analyser le contenu HTML
soup = BeautifulSoup(response.content, 'html.parser')

#print(soup)

montres = soup.find_all('article')
print(montres[4])


