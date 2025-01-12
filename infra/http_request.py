import requests
from infra.logger import logger
from infra.config import Config


class HttpRequest:

    # Initialize the API with base URL from Config
    def __init__(self):
        self.url = Config.URL


    # Make a GET request to the specified endpoint
    def get(self, endpoint: str, params=None):
        url = f"{self.url}/{endpoint}"
        try:
            r = requests.request('GET', url=url, params=params , headers={'accept': 'text/plain'})
            return r
        except requests.exceptions.RequestException as e:
            logger.error(f"Error during GET request to {url}: {str(e)}")


    # Make a POST request to the specified endpoint
    def post(self, endpoint: str, data=None, headers=None):
        url = f"{self.url}/{endpoint}"
        try:
            r = requests.request('POST', url=url, data=data, headers={'Content-Type': 'application/json'})
            return r
        except requests.exceptions.RequestException as e:
            logger.error(f"Error during POST request to {url}: {str(e)}")



    # Make a PUT request to the specified endpoint
    def put(self, endpoint: str, data=None, headers=None):
        url = f"{self.url}/{endpoint}"
        try:
            r = requests.request('PUT', url=url, data=data, headers={'Content-Type': 'application/json'})
            return r
        except requests.exceptions.RequestException as e:
            logger.error(f"Error during PUT request to {url}: {str(e)}")


    # Delete request to the specified endpoint
    def delete(self, endpoint: str, data=None, headers=None):
        url = f"{self.url}/{endpoint}"
        try:
            r = requests.request('DELETE', url=url, data=data, headers={'Content-Type': 'application/json'})
            return r
        except requests.exceptions.RequestException as e:
            logger.error(f"Error during DELETE request to {url}: {str(e)}")
