import requests
from bs4 import BeautifulSoup
import json

def kinopoisk(id):
    url = f'https://www.kinopoisk.ru/user/{id}/votes/'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        Data = []
        films = soup.find_all('div', class_='item')    
        for film in films:
            title = film.find('div', class_='nameRus').text.strip()
            Session = film.find('div', class_='date').text.strip()
            Data.append({'Name': title, 'Data': Session})   
            

        return Data
    
id = input('Введите id: ')
try:
    Data = kinopoisk(id)
    print(Data)
except:
    print("Ошибка!!!")

with open("result.json", "w", encoding='utf-8') as file:
    json.dump(Data, file, ensure_ascii=False)
