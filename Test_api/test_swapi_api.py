import pytest
from api.swapi_api import SWAPI


class TestAPI:
    @pytest.fixture()
    def api(self):
        base_url = "https://swapi.dev/api"
        return SWAPI(base_url)

    def test_get_films(self, api):
        response = api.get_films()
        response.raise_for_status()
        assert response.status_code == 200
        assert "results" in response.json()

    def test_get_planets(self, api):
        response = api.get_planets()
        response.raise_for_status()
        assert response.status_code == 200
        assert "results" in response.json()

    def test_get_starships(self, api):
        response = api.get_starships()
        response.raise_for_status()
        assert response.status_code == 200
        assert "results" in response.json()
