from logic.endpoints import Endpoints
from infra.crud_api import CrudApi

#Ask if there is need to add headers to the POST & GET

class PlaylistLogic:


    def __init__(self):
        self.api = CrudApi()

    # Add a specific song into a specific playlist
    def add_song(self, user_name: str, user_password: str, playlist_name: str, song_title: str):
        data = {
            "user_name": user_name,
            "user_password": user_password,
            "playlist_name": playlist_name,
            "song_title": song_title
        }
        return self.api.post(Endpoints.PLAYLISTS_ADD_SONG, data=data)

