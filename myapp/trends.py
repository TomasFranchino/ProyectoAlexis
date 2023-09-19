import requests
from bs4 import BeautifulSoup


url = 'https://ciberninjas.com/programacion/'


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


titulo = soup.find_all('h2', class_='entry-title')
titulos=[]
for i in titulo:
      titulos.append(i.text)


div= soup.find_all('div', class_='entry-summary')
links = []
contenidos = []
for div_element in div:
    p_elemento = div_element.find('p')
    a_elementos = div_element.find_all('a') 
    if p_elemento:
          texto = p_elemento.get_text()
          contenidos.append(texto)
    for a_elemento in a_elementos:
        enlace = a_elemento.get('href')
        links.append(enlace)


def TituloTendencias():
     return titulos
def ContenidoTendencias():
     return contenidos 
def UrlTendencias():
     return links
