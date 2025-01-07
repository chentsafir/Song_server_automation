import json
from pydantic import BaseModel

class Friend(BaseModel):

    user_name: str = None
    user_password: str = None
    friend_name: str = None


class User(BaseModel):
    user_name: str = None
    user_password: str = None
    user_new_password: str = None
    playlist_list: [] = None
    friend_list : [] = None


    def to_json(self):
        hh=(self.model_dump_json())
        return hh
