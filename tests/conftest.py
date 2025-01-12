import pytest

from logic.users import UserLogic
from logic.songs import SongLogic
from logic.playlists import PlaylistLogic
from logic.admin import AdminLogic

@pytest.fixture(scope="function")
def user_logic():
    user_logic1 = UserLogic()
    yield user_logic1

    #clean up after test
    admin=AdminLogic()
    admin.delete_all_users()
    admin.delete_all_songs()


@pytest.fixture(scope="function")
def song_logic():
    song_logic1 = SongLogic()
    yield song_logic1

    #clean up after test
    admin=AdminLogic()
    admin.delete_all_users()
    admin.delete_all_songs()


@pytest.fixture(scope="function")
def playlist_logic():
    playlist_logic1 = PlaylistLogic
    yield playlist_logic1

    # clean up after test
    admin = AdminLogic()
    admin.delete_all_users()
    admin.delete_all_songs()

