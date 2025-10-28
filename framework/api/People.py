import requests
from configuration.constants.APIpaths import APIpaths


class People:
    people_url = "people/"

    @staticmethod
    def get_people(people_id: int):
        _url = f"{APIpaths.BASE_URL}{APIpaths.PEOPLE_URL}{people_id}/"
        return requests.get(_url)