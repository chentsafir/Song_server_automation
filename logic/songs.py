from logic.endpoints import Endpoints
from infra.crud_api import CrudApi
from logic.song_schemas import SongRequest
import json

#Ask if there is need to add headers to the POST & GET

class SongLogic:
    def __init__(self):
        self.api = CrudApi()

    #Add a new song to the system
    def add_song(self, song_data : SongRequest):
        r=self.api.post(Endpoints.SONGS_ADD_SONG, data=song_data.to_json())
        return r

    #Downvote a song in system
    def downvote(self,  song_data : SongRequest):
        r=self.api.put(Endpoints.SONGS_DOWNVOTE, data=song_data.to_json())
        return r

    #Get information about a specific song
    def get_song(self, song_data : SongRequest):
        r=self.api.get(Endpoints.SONGS_GET_SONG, params=json.loads(song_data.to_json()))
        return r

    #Get ranked songs based on a specified rank and operator
    def get_ranked_songs(self, song_data : SongRequest):
        r=self.api.get(Endpoints.SONGS_RANKED_SONGS, params=json.loads(song_data.to_json()))
        return r

    #Upvote a song in system
    def upvote(self, song_data : SongRequest):
        r=self.api.put(Endpoints.SONGS_UPVOTE, data=song_data.to_json())
        return r