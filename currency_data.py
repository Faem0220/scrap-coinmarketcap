from bs4 import BeautifulSoup # Se importa librería para hacer scraping
import requests # Librería para peticiones HTTP
import time  # Librería para operaciones temporales
link = input('Inserte url de la currency >')

def currency_data(link):
    url = (f'https://coinmarketcap.com{link}')
    html_text = requests.get(url).text   
    soup = BeautifulSoup(html_text, 'lxml') 
    currency_body = soup.find('div', class_='sc-fzqARJ eLpUJW cmc-body-wrapper')
    currency_container = currency_body.find('div', class_='sc-AxhCb jGVDnv container')

    name_section = currency_container.find('div', class_='sc-AxhCb jDIFcq nameSection___3Hk6F')
    symbol = name_section.find('small', class_='nameSymbol___1arQV').text
    name = name_section.h2.text.replace(symbol,'')

    price_section = currency_container.find('div', class_='sc-AxhCb bYwLMj priceSection___3kA4m')
    us_price = price_section.find('div', class_='priceValue___11gHJ').text
    btc_price = price_section.find('p', class_='sc-10nusm4-0 bspaAT').text
    print(f'Nombre: {name}')
    print(f'Símbolo: {symbol}')
    print(f'USD price: {us_price}')
    print(f'BTC price: {btc_price}')
    stats_section = currency_container.find('div', class_='sc-AxhCb iOyrqq statsSection___2aZ29')
    stats_data = stats_section.find_all('div', class_='statsBlockInner___1abzU')
    for stat in stats_data:
        stats_name = stat.text.replace('$',': $')
        print(stats_name)
    supply_data = stats_section.find('div', class_='statsSupplyBlock___ST_Wb')
    circulating = supply_data.find('div',class_='statsValue___2iaoZ').text
    max_supply = supply_data.find('div',class_='sc-AxhCb jOwIxl').text.replace('y','y ')
    total_supply = supply_data.find('div',class_='sc-AxhCb kRgzVw').text.replace('y','y ')

    network = currency_body.find('div', class_='sc-AxhCb bYwLMj container___2dCiP contractsRow')
    main_chain = network.find('div',class_='mainChain___3CfU2').span.text
    print(f'Circulating supply: {circulating}')
    print(f'Max supply: {max_supply}')
    print(f'Total supply: {total_supply}')
    print(f'Main Network: {main_chain}')
    
    
if __name__ == '__main__':  #Para automatizar el programa y que se ejecute cada 10 minutos
        currency_data(link)
      