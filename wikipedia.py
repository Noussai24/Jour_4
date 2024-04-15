import requests
from bs4 import BeautifulSoup

# URL de la page Wikipedia sur la chimie
url = "https://fr.wikipedia.org/wiki/Chimie"

# Faire une requête pour obtenir le contenu de la page
response = requests.get(url)
content = response.content

# Utiliser BeautifulSoup pour analyser le contenu HTML de la page
soup = BeautifulSoup(content, 'html.parser')

# Trouver l'élément <div> avec la classe "mw-mmv-image"
div_class = soup.find("div", {"class":"mw-mmv-image-wrapper"})
if div_class:
    image = div_class.find('img')
    if image:
        img_source = image.get('src')
    else:
        print("bla")
else:
    print("blabla")

# Afficher l'élément trouvé
print(div_class)

git add .
