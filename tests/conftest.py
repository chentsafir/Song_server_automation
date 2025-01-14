import pytest
from infra.config import Config
from logic.song_server_api import ClientApi
from infra.logger import logger


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "no_cleanup: mark test to skip cleanup"
    )


@pytest.fixture(scope="function", autouse=True)
def clean_up(request):
    if not request.node.get_closest_marker("no_cleanup"):
        logger.info("Running regular cleanup")
        yield
        admin = ClientApi(host=Config.HOST)
        admin.delete_all_users()
        admin.delete_all_songs()
    else:
        logger.info("Skipping regular cleanup due to no_cleanup marker")
        yield



@pytest.fixture(scope="function")
def api():
    client_api = ClientApi(host=Config.HOST)
    yield client_api
