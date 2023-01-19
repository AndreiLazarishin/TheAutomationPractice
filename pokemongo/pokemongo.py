import logging

import pytest
import requests

from conftest import POKEMON_URL, indexes_76_data, indexes_132_data


class TestsPokemon:
    log = logging.getLogger(__name__)

    def test_check_limber_details(self, limber_abilities_object):
        """Checking if limber data is correct"""
        response = requests.get(url=POKEMON_URL).json()
        assert limber_abilities_object.slot == response['abilities'][0]['slot']
        assert limber_abilities_object.is_hidden == response['abilities'][0]['is_hidden']
        assert response['abilities'][0]['ability']['name'] == limber_abilities_object.name
        assert limber_abilities_object.url == response['abilities'][0]['ability']['url']

    def test_imposter_find(self, imposter_abilities_object):
        """Checking if imposter data is correct"""
        response = requests.get(url=f'{POKEMON_URL}?offset=140').json()
        assert imposter_abilities_object.slot == response['abilities'][1]['slot']
        assert imposter_abilities_object.is_hidden == response['abilities'][1]['is_hidden']
        assert imposter_abilities_object.name in response['abilities'][1]['ability']['name']
        assert imposter_abilities_object.url == response['abilities'][1]['ability']['url']

    def test_base_experience(self):
        response = requests.get(url=POKEMON_URL).json()
        assert response['base_experience'] == 101  # probably should set it as a variable???

    def test_forms_ditto(self, ditto_forms_object):
        """Checking if ditto_forms data is correct"""
        response = requests.get(url=f'{POKEMON_URL}?offset=130').json()
        assert ditto_forms_object.name in response['forms'][0]['name']
        assert ditto_forms_object.url == response['forms'][0]['url']

    @pytest.mark.parametrize('game_index, name, url', indexes_76_data)
    def test_game_76_indices(self, game_index, name, url):
        response = requests.get(url=POKEMON_URL).json()
        assert name in response['game_indices'][0]['version']['name']
        assert url in response['game_indices'][0]['version']['url']
        assert game_index == response['game_indices'][0]['game_index']

    # TODO Try to parametrize tests [blue, yellow]

    @pytest.mark.parametrize('game_index, name, url', indexes_132_data)
    def test_game_132_indices(self, game_index, name, url, game_indexes_object):
        response = requests.get(url=POKEMON_URL).json()
        assert name in response['game_indices'][0]['version']['name']
        assert url in response['game_indices'][0]['version']['url']
        assert game_index == response['game_indices'][0]['game_index']
        assert game_indexes_object.height == response['height']
