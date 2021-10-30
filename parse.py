from bs4 import BeautifulSoup
import requests

class Asaxiy():
    HEADERS = {'user_agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36',
               'accept': '*/*'}

    def __init__(self, url):
        self.url = url


    def get_html(self, params=None):
        r = requests.get(self.url, headers=self.HEADERS, params=params)
        return r

    def get_title(self):
        html = self.get_html()
        soup = BeautifulSoup(html.text, 'html.parser')
        titles = soup.find_all('div', class_='item__small-info')

        title = []
        for titled in titles:
            title.append(titled.find('div', class_='item__small-heading').get_text(strip=True))
        return title

    def get_price(self):
        html = self.get_html()
        soup = BeautifulSoup(html.text, 'html.parser')
        prices = soup.find_all('div', class_='item__small-info')

        price = []
        for priced in prices:
            price.append(priced.find('div', class_='item__small--prices').get_text(strip=True))
        return price

    def get_photo(self):
        html = self.get_html()
        soup = BeautifulSoup(html.text, 'html.parser')
        photos = soup.find_all('div', class_='item__small-img')

        photo = []
        for priced in photos:
            photo.append(priced.find('img', class_='lazyload').get('data-src'))
        return photo