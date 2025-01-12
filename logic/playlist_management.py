from pydantic import BaseModel


class PlayLists(BaseModel):
    user_name : str = None
    user_password : str = None
    playlist_name : str = None
    song_title: str = None

    def to_json(self):
        j=(self.model_dump_json())
        return j