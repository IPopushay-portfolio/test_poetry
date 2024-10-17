import requests

API_KEY = "6xVHX1YfwYtA1ZjWACCbKPfvzl6SiNaO"
url = "https://api.apilayer.com/exchangerates_data/convert"
headers = {"apikey": "6xVHX1YfwYtA1ZjWACCbKPfvzl6SiNaO"}
response = requests.get(url, headers=headers)
