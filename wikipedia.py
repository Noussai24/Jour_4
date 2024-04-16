
# J'importe le module 'requests' de la bibliothèque 'requests' pour envoyer des requêtes HTTP et récupérer le contenu des pages web.
# J'importe BeautifulSoup du module 'bs4' de la bibliothèque 'BeautifulSoup' pour analyser et extraire des données à partir du contenu HTML.
import requests
from bs4 import BeautifulSoup

# Je déclare l'URL de la page Wikipedia sur la chimie que je souhaite analyser.
url = "https://fr.wikipedia.org/wiki/Chimie"

# Je fais une requête HTTP à l'URL spécifiée en utilisant la fonction 'get' du module 'requests' pour obtenir le contenu de la page.
response = requests.get(url)
content = response.content

# J'utilise BeautifulSoup pour analyser le contenu HTML de la page en créant un objet BeautifulSoup à partir du contenu HTML récupéré.
# BeautifulSoup utilise le parseur HTML intégré 'html.parser' pour analyser le contenu et le transformer en une structure de données exploitable.
soup = BeautifulSoup(content, 'html.parser')

# Je recherche la première balise <img> dans le contenu HTML de la page analysée.
img = soup.find('img')

# Je printe la balise <img> trouvée dans la console.
print(img)



# Trouver la première balise <img> sur la page
# Recherche de la première balise <img> dans le contenu HTML de la page analysée.
img = soup.find('img')

# Afficher la balise <img> trouvée
# Affichage de la balise <img> trouvée dans la console.
print(img)


