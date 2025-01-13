import pytest
from infra.config import Config
from logic.song_server_api import ClientApi
from logic.user_management import User




@pytest.fixture(scope="function", autouse=True) #autouse for teardown function without call clean_up
def clean_up():
    yield
    #clean up after test
    admin = ClientApi(host=Config.HOST)
    admin.delete_all_users()
    admin.delete_all_songs()



@pytest.fixture(scope="function")
def api():
    client_api = ClientApi(host=Config.HOST)
    yield client_api
