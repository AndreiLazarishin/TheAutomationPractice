import requests

# import rest_assured

URL = 'https://pokeapi.co/api/v2/ability/battle-armor'
# response = requests.request(method='GET', url=f"{URL}/ability/{name}")
response = requests.get(url='https://pokeapi.co/api/v2/language/6/')
print(response.status_code)
print(response.text)
