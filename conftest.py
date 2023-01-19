import pytest

from pokemongo.pokemon_objects import PokemonData

POKEMON_URL = 'https://pokeapi.co/api/v2/pokemon/ditto/'


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
    (76, 'red', "https://pokeapi.co/api/v2/version/1/"),
    (76, 'blue', "https://pokeapi.co/api/v2/version/2/"),
    (76, 'yellow', "https://pokeapi.co/api/v2/version/3/")
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
