import requests


class SWAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_films(self):
        response = requests.get(f"{self.base_url}/films/")
        return response

    def get_planets(self):
        response = requests.get(f"{self.base_url}/planets/")
        return response

    def get_starships(self):
        response = requests.get(f"{self.base_url}/starships/")
        return response
