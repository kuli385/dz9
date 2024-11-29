import requests

from bs4 import BeautifulSoup

class CurrencyConverter:

   def __init__(self):

       self.url = 'https://bank.gov.ua/'

       self.currency_dict = {}

       self.get_currency_dict()

   def get_currency_dict(self):

       response = requests.get(self.url)

       soup = BeautifulSoup(response.content, 'html.parser')

       table = soup.find('table', {'class': 'data'})

       rows = table.tbody.find_all('tr')

       for row in rows:

           cols = row.find_all('td')

           if len(cols) > 1:

               currency_name = cols[1].text.strip()

               currency_rate = cols[4].text.strip().replace(',', '.')

               self.currency_dict[currency_name] = float(currency_rate)

   def convert(self, amount, from_currency, to_currency):

       initial_amount = amount

       if from_currency != 'USD':

           amount = amount / self.currency_dict[from_currency]

       # limiting the precision to 4 decimal places

       amount = round(amount * self.currency_dict[to_currency], 4)

       return amount

# Пример использования класса конвертера валют

currency_converter = CurrencyConverter()

print(currency_converter.convert(1000, 'UAH', 'USD'))