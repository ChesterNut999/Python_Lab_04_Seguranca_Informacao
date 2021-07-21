from bs4 import BeautifulSoup
import requests

# Objeto site recebendo o conteúdo do requisição
site = requests.get('https://www.climatempo.com.br/').content

# Objeto soup baixando o HTML
soup = BeautifulSoup(site, 'html-parser')

# Transforma o HTML em String
# print(soup.prettify())
temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
print(temperatura.string)
