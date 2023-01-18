import pytest

from pokemongo.pokemon_objects import PokemonData


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
