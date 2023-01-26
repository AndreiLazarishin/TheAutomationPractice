import json

import pytest
import requests
from selenium import webdriver

from constants.base import BASE_URL, DRIVER_PATH
from pages.start_page import StartPage
from pokemongo.pokemon_objects import PokemonData

pokemon_ditto_api_response = requests.get(url='https://pokeapi.co/api/v2/pokemon/ditto/').json()
pokemon_species_api_response = requests.get(url='https://pokeapi.co/api/v2/pokemon-species/aegislash').json()
pokemon_type_api_response = requests.get(url='https://pokeapi.co/api/v2/type/3').json()
pokemon_battle_armor_api_response = requests.get(url='https://pokeapi.co/api/v2/ability/battle-armor').json()

with open('pokemon_ditto.json', 'w') as file:
    json.dump(pokemon_ditto_api_response, file, indent=2)

with open('pokemon_species.json', 'w') as file:
    json.dump(pokemon_species_api_response, file, indent=2)

with open('pokemon_type.json', 'w') as file:
    json.dump(pokemon_type_api_response, file, indent=2)

with open('pokemon_battle_armor.json', 'w') as file:
    json.dump(pokemon_battle_armor_api_response, file, indent=2)


@pytest.fixture(scope='function')
def start_page():
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(BASE_URL)
    driver.implicitly_wait(1.5)
    yield StartPage(driver)
    driver.close()


@pytest.fixture()
def limber_abilities_object():
    limber = PokemonData()
    limber.name = 'limber'
    limber.url = "https://pokeapi.co/api/v2/ability/7/"
    limber.is_hidden = False
    limber.slot = 1
    return limber


@pytest.fixture()
def imposter_abilities_object():
    limber = PokemonData()
    limber.name = 'imposter'
    limber.url = "https://pokeapi.co/api/v2/ability/150/"
    limber.is_hidden = True
    limber.slot = 3
    return limber


@pytest.fixture()
def ditto_forms_object():
    ditto = PokemonData()
    ditto.name = 'ditto'
    ditto.url = "https://pokeapi.co/api/v2/pokemon-form/132/"
    return ditto


indexes_76_data = [
    (76, 0, 'red', "https://pokeapi.co/api/v2/version/1/"),
    (76, 1, 'blue', "https://pokeapi.co/api/v2/version/2/"),
    (76, 2, 'yellow', "https://pokeapi.co/api/v2/version/3/")
]

indexes_132_data = [
    (132, 'gold', "https://pokeapi.co/api/v2/version/4/"),
    (132, 'silver', "https://pokeapi.co/api/v2/version/5/"),
    (132, 'crystal', "https://pokeapi.co/api/v2/version/6/"),
    (132, 'ruby', "https://pokeapi.co/api/v2/version/7/"),
    (132, 'sapphire', "https://pokeapi.co/api/v2/version/8/"),
    (132, 'emerald', "https://pokeapi.co/api/v2/version/9/"),
    (132, 'firered', "https://pokeapi.co/api/v2/version/10/"),
    (132, 'leafgreen', "https://pokeapi.co/api/v2/version/11/"),
    (132, 'diamond', "https://pokeapi.co/api/v2/version/12/"),
    (132, 'pearl', "https://pokeapi.co/api/v2/version/13/"),
    (132, 'platinum', "https://pokeapi.co/api/v2/version/14/"),
    (132, 'heartgold', "https://pokeapi.co/api/v2/version/15/"),
    (132, 'soulsilver', "https://pokeapi.co/api/v2/version/16/"),
    (132, 'black', "https://pokeapi.co/api/v2/version/17/"),
    (132, 'white', "https://pokeapi.co/api/v2/version/18/"),
    (132, 'black-2', "https://pokeapi.co/api/v2/version/21/"),
    (132, 'white-2', "https://pokeapi.co/api/v2/version/22/")
]

# url

held_items_0_version_data = [
    (5, 'ruby', "https://pokeapi.co/api/v2/version/7/"),
    (5, "sapphire", "https://pokeapi.co/api/v2/version/8/"),
    (5, "emerald", "https://pokeapi.co/api/v2/version/9/"),
    (5, "firered", "https://pokeapi.co/api/v2/version/10/"),
    (5, "leafgreen", "https://pokeapi.co/api/v2/version/11/"),
    (5, "diamond", "https://pokeapi.co/api/v2/version/12/"),
    (5, "pearl", "https://pokeapi.co/api/v2/version/13/"),
    (5, "platinum", "https://pokeapi.co/api/v2/version/14/"),
    (5, "heartgold", "https://pokeapi.co/api/v2/version/15/"),
    (5, "soulsilver", "https://pokeapi.co/api/v2/version/16/"),
    (5, "black", "https://pokeapi.co/api/v2/version/17/"),
    (5, "white", "https://pokeapi.co/api/v2/version/18/"),
    (5, "black-2", "https://pokeapi.co/api/v2/version/21/"),
    (5, "white-2", "https://pokeapi.co/api/v2/version/22/"),
    (5, "x", "https://pokeapi.co/api/v2/version/23/"),
    (5, "y", "https://pokeapi.co/api/v2/version/24/"),
    (5, "omega-ruby", "https://pokeapi.co/api/v2/version/25/"),
    (5, "alpha-sapphire", "https://pokeapi.co/api/v2/version/26/"),
    (5, "sun", "https://pokeapi.co/api/v2/version/27/"),
    (5, "moon", "https://pokeapi.co/api/v2/version/28/"),
    (5, "ultra-sun", "https://pokeapi.co/api/v2/version/29/"),
    (5, "ultra-moon", "https://pokeapi.co/api/v2/version/30/"),
]


@pytest.fixture()
def game_indexes_object():
    color = PokemonData()
    color.height = 3
    return color


@pytest.fixture()
def gold_indexes_object():
    gold = PokemonData()
    gold.name = 'gold'
    gold.url = "https://pokeapi.co/api/v2/version/4/"
    gold.game_index = 132
    return gold


@pytest.fixture()
def elements_page():
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(BASE_URL)
    driver.implicitly_wait(1.5)
    yield StartPage(driver)
    driver.close()
