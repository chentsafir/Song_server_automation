import json
from pydantic import BaseModel


class Songs(BaseModel):
    song_title: str =None
    song_performer: str =None
    song_genre: str =None
    song_year: str =None
    user_name: str =None
    user_password: str =None
    playlist_name: str =None
    rank: str=None
    op: str=None


    def to_json(self):
        return (self.model_dump_json())


