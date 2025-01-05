from logic.endpoints import Endpoints
from infra.crud_api import CrudApi


#Ask if there is need to add headers to the POST & GET

class SongLogic:
    def __init__(self):
        self.api = CrudApi()

    #Add a new song to the system
    def add_song(self, song_title: str, song_performer: str, song_genre: str, song_year: str):
        data = {
            "song_title": song_title,
            "song_performer": song_performer,
            "song_genre": song_genre,
            "song_year": song_year
        }
        return self.api.post(Endpoints.SONGS_ADD_SONG, data=data)

    #Downvote a song in system
    def downvote(self, user_name: str, user_password: str, playlist_name: str, song_title: str):
        data = {
            "user_name": user_name,
            "user_password": user_password,
            "playlist_name": playlist_name,
            "song_title": song_title
        }
        return self.api.put(Endpoints.SONGS_DOWNVOTE, data=data)

    #Get information about a specific song
    def get_song(self, song_title: str):
        params = {
            "song_title": song_title
        }
        return self.api.get(Endpoints.SONGS_GET_SONG, params=params)

    #Get ranked songs based on a specified rank and operator
    def get_ranked_songs(self, rank: str, op: str):
        params = {
            "rank": rank,
            "op": op
        }
        return self.api.get(Endpoints.SONGS_RANKED_SONGS, params=params)

    #Upvote a song in system
    def upvote(self, user_name: str, user_password: str, playlist_name: str, song_title: str):
        data = {
            "user_name": user_name,
            "user_password": user_password,
            "playlist_name": playlist_name,
            "song_title": song_title
        }
        return self.api.put(Endpoints.SONGS_UPVOTE, data=data)