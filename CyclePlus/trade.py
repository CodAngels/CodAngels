#This should use the trade sequences from @money.py to trade.
#It should be able to repeatedly trade throughout the day and night 
#It should send the amount of profits made after each day to a gmail account of my choosing


#The platform to obtain the real currency rates is @xe.com API 

import requests

url = 'https://xe.com/xecurrencydata/api/latest'
api_key = '3oquusq4mkfdbfsj11kp6tnjhr'  # replace with your XE Currency Data API key

headers = {
    'Authorization': f'Bearer {api_key}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    rates = data['rates']
    currencies = list(rates.keys())

    exchange_matrix = []
    for currency1 in currencies:
        exchange_row = []
        for currency2 in currencies:
            exchange_rate = rates[currency2] / rates[currency1]
            exchange_row.append(exchange_rate)
        exchange_matrix.append(exchange_row)

    print('Exchange matrix:')
    for row in exchange_matrix:
        print(row)

    print('Currencies:')
    print(currencies)

else:
    print(f'Request failed with status code {response.status_code}')
