import requests
import json
from infra.config import Config


class CrudApi:

    # Initialize the API with base URL from Config
    def __init__(self):
        self.url = Config.URL

    # Make a GET request to the specified endpoint
    def get(self, endpoint: str, params=None):
        url = f"{self.url}/{endpoint}"
        r = requests.request('GET', url=url, params=params , headers={'accept': 'text/plain'})  # requests.get will not send query parameters if param=None
        return r
        # Make a POST request to the specified endpoint

    def post(self, endpoint: str, data=None, headers=None):
        url = f"{self.url}/{endpoint}"
        r = requests.request('POST', url=url, data=data, headers={'Content-Type': 'application/json'})
        return r


    # Make a PUT request to the specified endpoint
    def put(self, endpoint: str, data=None, headers=None):
        url = f"{self.url}/{endpoint}"
        r = requests.request('PUT', url=url, data=data, headers={'Content-Type': 'application/json'})
        return r

    # Delete request to the specified endpoint
    def delete(self, endpoint: str, data=None, headers=None):
        url = f"{self.url}/{endpoint}"
        r = requests.request('DELETE', url=url, data=data, headers={'Content-Type': 'application/json'})
        return r
