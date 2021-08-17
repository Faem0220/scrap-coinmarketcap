from bs4 import BeautifulSoup # Se importa librería para hacer scraping
import requests # Librería para peticiones HTTP
import time  # Librería para operaciones temporales

print(f'Ingrese URL de coinmarketcap:')  # Una interfaz para hacer pruebas de entrada

url = input('>')

def obtain_name():

    html_text = requests.get(url).text
    
    soup = BeautifulSoup(html_text, 'lxml') # Se utiliza lxlm como parser

    currencies_table = soup.find('div', class_='tableWrapper___3utdq cmc-table-homepage-wrapper___22rL4') #Se filtra la tabla de currencies

    currency_name = currencies_table.find_all('a', class_="cmc-link") #Se filtra por la columna Name de la tabla. SOLO FILTRA DE A 10 LUEGO CAMBIA EL NOMBRE DE LA CLASS
    for currency2 in currency_name:

        link = currency2['href']
        name = link[12:].replace('/markets/', '')
        clean = name.replace('/','')
        print(f'Nombre:{clean}')
        print(f'URL:{link}')
        print('')

if __name__ == '__main__':  #Para automatizar el programa y que se ejecute cada 10 minutos
        obtain_name()