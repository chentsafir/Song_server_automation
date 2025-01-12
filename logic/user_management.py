import json
from pydantic import BaseModel

class PlayList(BaseModel):
    playlist_name: str =None
    user_name: str = None
    user_password: str = None

class Friend(BaseModel):
    user_name: str = None
    user_password: str = None
    friend_name: str = None


class User(BaseModel):
    user_name: str
    user_password: str
    user_new_password: str = None
    playlist_list: list[PlayList] = None
    friend_list : list[Friend] = None


    def to_json(self):
        j=(self.model_dump_json())
        return j
