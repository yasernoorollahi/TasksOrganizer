import requests

BASE= 'http://127.0.0.1:50001/'

response = requests.get(BASE+'users')
print(response.json())