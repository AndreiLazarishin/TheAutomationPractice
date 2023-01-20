import json
import logging

import requests


class TestsPokemon:
    log = logging.getLogger(__name__)

    def test_ditto_equals(self):
        """Confirm that json data and ditto API response are equal"""
        with open('pokemon_ditto.json') as file:
            json_pokemon_file = json.load(file)
        assert json_pokemon_file == requests.get(url='https://pokeapi.co/api/v2/pokemon/ditto/').json()

    def test_species_equals(self):
        """Confirm that json data and species API response are equal"""
        with open('pokemon_species.json') as file:
            json_species_file = json.load(file)
        assert json_species_file == requests.get(url='https://pokeapi.co/api/v2/pokemon-species/aegislash').json()

    def test_type_equals(self):
        """Confirm that json data and types API response are equal"""
        with open('pokemon_type.json') as file:
            json_type_file = json.load(file)
        assert json_type_file == requests.get(url='https://pokeapi.co/api/v2/type/3').json()

    def test_battle_armor_equals(self):
        """Confirm that json data and battle_armor API response are equal"""
        with open('pokemon_battle_armor.json') as file:
            json_battle_armor_file = json.load(file)
        assert json_battle_armor_file == requests.get(url='https://pokeapi.co/api/v2/ability/battle-armor').json()

    # def test_check_limber_details(self, limber_abilities_object):
    #     """Checking if limber data is correct"""
    #     response = requests.get(url=POKEMON_URL).json()
    #     assert limber_abilities_object.slot == response['abilities'][0]['slot']
    #     assert limber_abilities_object.is_hidden == response['abilities'][0]['is_hidden']
    #     assert response['abilities'][0]['ability']['name'] == limber_abilities_object.name
    #     assert limber_abilities_object.url == response['abilities'][0]['ability']['url']  # data provider
    #
    # def test_imposter_find(self, imposter_abilities_object):
    #     """Checking if imposter data is correct"""
    #     response = requests.get(url=f'{POKEMON_URL}?offset=140').json()
    #     assert imposter_abilities_object.slot == response['abilities'][1]['slot']
    #     assert imposter_abilities_object.is_hidden == response['abilities'][1]['is_hidden']
    #     assert imposter_abilities_object.name in response['abilities'][1]['ability']['name']
    #     assert imposter_abilities_object.url == response['abilities'][1]['ability']['url']

    # def test_base_experience(self):
    #     response = requests.get(url=POKEMON_URL).json()
    #     assert response['base_experience'] == 101  # probably should set it as a variable???
    #
    # def test_forms_ditto(self, ditto_forms_object):
    #     """Checking if ditto_forms data is correct"""
    #     response = requests.get(url=f'{POKEMON_URL}?offset=130').json()
    #     assert ditto_forms_object.name in response['forms'][0]['name']
    #     assert ditto_forms_object.url == response['forms'][0]['url']
    #
    # @pytest.mark.parametrize('game_index, object_index, name, url', indexes_76_data)
    # def test_game_76_indices(self, game_index, object_index, name, url):
    #
    #     response = requests.get(url=POKEMON_URL).json()
    #     assert name in response['game_indices'][object_index]['version']['name']
    #     assert url in response['game_indices'][object_index]['version']['url']
    #     assert game_index == response['game_indices'][object_index]['game_index']
    #
    # @pytest.mark.parametrize('game_index, name, url', indexes_132_data)
    # def test_game_132_indices(self, game_index, name, url, game_indexes_object):
    #     response = requests.get(url=POKEMON_URL).json()
    #     assert name in response['game_indices'][0]['version']['name']
    #     assert url in response['game_indices'][0]['version']['url']
    #     assert game_index == response['game_indices'][0]['game_index']
    #     assert game_indexes_object.height == response['height']
