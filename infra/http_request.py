import requests
from infra.logger import logger


HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}


# Make a GET request to the specified endpoint
def get(host, path, params=None, headers: dict | None = None):
    try:
        r = requests.get(url='http://' + host + path, headers=HEADERS, params=params)
        return r
    except requests.exceptions.RequestException as e:
        logger.error(f"Error during GET request to http://{host+path}: {str(e)}")


# Make a POST request to the specified endpoint
def post(host, path, json_data, headers: dict | None = None):
    try:
        r = requests.post(url='http://' + host + path, headers=HEADERS, json=json_data)
        return r
    except requests.exceptions.RequestException as e:
        logger.error(f"Error during POST request to http://{host+path} : {str(e)}")


# Make a PUT request to the specified endpoint
def put(host, path, json_data, headers: dict | None = None):
    try:
        r = requests.put(url='http://' + host + path, headers=HEADERS, json=json_data)
        return r
    except requests.exceptions.RequestException as e:
        logger.error(f"Error during PUT request to http://{host+path} : {str(e)}")


# Delete request to the specified endpoint
def delete(host, path):
    try:
        r = requests.delete(url='http://' + host + path)
        return r
    except requests.exceptions.RequestException as e:
        logger.error(f"Error during DELETE request to http://{host+path}: {str(e)}")
