from bs4 import BeautifulSoup # Se importa librería para hacer scraping
import requests # Librería para peticiones HTTP
import time  # Librería para operaciones temporales


print(f'Ingrese URL de coinmarketcap:')  # Una interfaz para hacer pruebas de entrada
url = input('>')

def currency_list():
    html_text = requests.get(url).text #se extrae el html de la página

    soup = BeautifulSoup(html_text, 'lxml') # Se utiliza lxlm como parser

    currencies_table = soup.find('table', class_='cmc-table cmc-table___11lFC cmc-table-homepage___2_guh') #Se filtra la tabla de currencies

    currency_name = currencies_table.find_all('div', class_='sc-AxhCb bXGzHn') #Se filtra por la columna Name de la tabla. SOLO FILTRA DE A 10 LUEGO CAMBIA EL NOMBRE DE LA CLASS

    for currency in currency_name:  # Se recorre la tabla para extraer todos los nombres y links
        name = currency.find('div', class_='sc-AxhCb sc-fzoaKM cbJhSy').p.text
        link = currency.a['href']
        print(name)
        print(link)

if __name__ == '__main__':  #Para automatizar el programa y que se ejecute cada 10 minutos
    while True:
        currency_list()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)









