import json
from pydantic import BaseModel
from pydantic_core import to_json


class PlayList(BaseModel):
    playlist_name: str =None
    # user_name: str = None
    # user_password: str = None

class Friend(BaseModel):
    # user_name: str = None
    # user_password: str = None
    friend_name: str = None


class User(BaseModel):
    user_name: str
    user_password: str
    playlist_list: list[PlayList] = None
    friend_list : list[Friend] = None


    #Transfer to dict and clean None parameters and return json
    def prepare(self):
        # Create dictionary from object
        data = self.model_dump()
        # Initialize empty dictionary for cleaned data
        cleaned_data = {}
        # Iterate through key-value pairs and add non-None values
        for key, value in data.items():
            if value is not None:
                cleaned_data[key] = value
        cleaned_data=json.dumps(cleaned_data)
        return cleaned_data

    #Transfer
    def to_json(self):
        j=self.model_dump_json()
        return j
