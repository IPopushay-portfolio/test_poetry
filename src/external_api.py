import os

import requests
from dotenv import load_dotenv


def conversion_currency(to_cur, from_cur, amount):
    load_dotenv()
    apikey = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_cur}&from={from_cur}&amount={amount})"
    headers = {"apikey": apikey}
    response = requests.get(url, headers=headers)
    result = response.json()
    return result


# data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=YOUR_API_KEY&q=USD_RUB&compact=ultra').json()
# print (data)


if __name__ == "__main__":
    print(conversion_currency("RUB", "USD", "200000"))
