import requests
from configuration.constants.APIpathes import APIpathes


class People:
    people_url = "people/"

    @staticmethod
    def get_people(people_id: int):
        _url = f"{APIpathes.BASE_URL}{APIpathes.PEOPLE_URL}{people_id}/"
        return requests.get(_url)