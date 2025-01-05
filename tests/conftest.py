import pytest

from logic.users import UserLogic
from logic.songs import SongLogic
from logic.playlists import PlaylistLogic
from logic.admin import AdminLogic

@pytest.fixture(scope="function")
def user_logic():
    user_logic = UserLogic()
    yield user_logic

    #clean up after test
    admin=AdminLogic()
    admin.delete_all_users()
    admin.delete_all_songs()


@pytest.fixture(scope="function")
def song_logic():
    song_logic = SongLogic()
    yield song_logic

    #clean up after test
    admin=AdminLogic()
    admin.delete_all_users()
    admin.delete_all_songs()


@pytest.fixture(scope="function")
def playlist_logic():
    playlist_logic = PlaylistLogic
    yield playlist_logic

    # clean up after test
    admin = AdminLogic()
    admin.delete_all_users()
    admin.delete_all_songs()