#pip instal bs4
import requests
from bs4 import BeautifulSoup
url = "https://decoplante.fr"

response = requests.get(url)
# print (response)
content = response.content
print (content)

soup = BeautifulSoup (content,'html')
img = soup.find('img')
#print(img)



