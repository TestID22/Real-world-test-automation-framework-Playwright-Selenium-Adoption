import requests

from framework.api.People import People


class API:
    token = None
    endpoint = 'https://swapi.py4e.com/api/'

    def autorize(self):
        pass

    def get(self, url):
        requests.get(url)

    @property
    def people(self):
        return People()

