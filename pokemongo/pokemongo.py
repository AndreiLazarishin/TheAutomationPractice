import requests

URL = 'https://pokeapi.co/api/v2/pokemon/ditto/'


class TestsPokemon:

    def test_check_limber_details(self, limber_abilities_object):
        response = requests.get(url=URL).json()
        assert limber_abilities_object.slot == response['abilities'][0]['slot']
        assert limber_abilities_object.is_hidden == response['abilities'][0]['is_hidden']
        assert response['abilities'][0]['ability']['name'] == limber_abilities_object.name
        assert limber_abilities_object.url == response['abilities'][0]['ability']['url']

    def test_imposter_find(self, imposter_abilities_object):
        response = requests.get(url=f'{URL}?offset=140').json()
        assert imposter_abilities_object.slot == response['abilities'][1]['slot']
        assert imposter_abilities_object.is_hidden == response['abilities'][1]['is_hidden']
        assert imposter_abilities_object.name in response['abilities'][1]['ability']['name']
        assert imposter_abilities_object.url == response['abilities'][1]['ability']['url']

    def test_forms_ditto(self, ditto_forms_object):
        response = requests.get(url=f'{URL}?offset=130').json()
        assert ditto_forms_object.name in response['forms'][0]['name']
        assert ditto_forms_object.url == response['forms'][0]['url']
