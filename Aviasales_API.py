
# https://app.travelpayouts.com/programs/100/tools/api
# ЗАПРОС: Самые дешевые билеты на определенные даты
# http://api.travelpayouts.com/v1/prices/direct
# https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin=MOW&destination=DXB&currency=usd&departure_at=2022-03-01&return_at=2022-03-10&sorting=price&direct=true&limit=10&token=РазместитеЗдесьВашТокен

# Параметры запроса
# origin — IATA-код города вылета. IATA-код указывается буквами верхнего регистра, например, MOW.
# destination — IATA-код города назначения (укажите «-" для любых направлений, например, &destination=&). IATA-код указывается буквами верхнего регистра, например, MOW.
# depart_date (необязательно) — месяц вылета (YYYY-MM).
# return_date (необязательно) — месяц возвращения (YYYY-MM).
# currency — валюта ответа (USD, EUR, RUB). Значение по умолчанию — rub.
# token — индивидуальный токен доступа.

import requests
import json
from pprint import pprint

api_key = 'TOKEN'
departure = 'MOW'
destination = 'DXB'
currency = 'usd'
departure_at = '2022-03-01'
return_at = '2022-03-10'
sorting = 'price'
direct = 'true'
limit = '10'
url = f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
params = {'origin': departure,
          'destination': destination,
          'currency': currency,
          'departure_at': departure_at,
          'return_at': return_at,
          'sorting': sorting,
          'direct': direct,
          'limit': limit,
          'token': api_key}

response = requests.get(url, params=params)
j_data = response.json()
# не получилось сделать как на уроке
# print(f"Самый дешевый билет из {j_data.get('origin')} в {j_data.get('destination')} {j_data.get('price')}")

pprint(j_data)

try:
    with open('Aviasales.json', 'w') as f:
      json.dump(j_data, f, ensure_ascii=False, indent=4)
    print("File saved")
except:
    print("File Failed")
