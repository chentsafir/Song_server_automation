import json
import typing
from pydantic import BaseModel



class User(BaseModel):
    user_name: str = None
    user_password: str = None
    friend_name:str = None
    playlist_name : str = None
    user_new_password:str = None
    playlist_list: typing.Optional[list['PlayList']] = None
    friend_list: typing.Optional[list['Friend']] = None

    # Transfer to dict and clean None parameters and return json
    def prepare(self):
        # Create dictionary from object
        data = self.model_dump()
        # Initialize empty dictionary for cleaned data
        cleaned_data = {}
        # Iterate through key-value pairs and add non-None values
        for key, value in data.items():
            if value is not None:
                cleaned_data[key] = value
        cleaned_data = json.dumps(cleaned_data)
        return cleaned_data

    def convert_username_to_params_dict(self):
        user_name_dict={"user_name": self.user_name}
        return user_name_dict


    # Transfer Pydantic Model to dict
    def to_json(self):
        j = self.model_dump()
        return j

    # Updates the User object with data received from server response
    def update_data(self, response_data: dict):
        data = response_data.get("data", {})

        # Map server response fields to object fields
        if "user_name" in data:
            self.user_name = data["user_name"]
        if "playlists" in data:
            playlist_data = data["playlists"]
            self.playlist_list = []
            for playlist_name in playlist_data:
                self.playlist_list.append(PlayList(playlist_name=playlist_name))
        if "friends" in data:
            friends_data = data["friends"]
            self.friend_list = []
            for friend_name in friends_data:
                self.friend_list.append(Friend(friend_name=friend_name))

        return self

    #Updates the user's password with the new password if exists.
    def update_password(self):
        if self.user_new_password:
            self.user_password = self.user_new_password
            self.user_new_password = None  # Clear the new password field (if we would like to change pass again)
        return self

    #Prepares the data for a change password request.
    def prepare_change_password_request(self):
        return {
            "user_name": self.user_name,
            "user_password": self.user_password,
            "user_new_password": self.user_new_password
        }


class PlayList(BaseModel):
    playlist_name: str

    #Prepares parameters for add_playlist request
    def prepare_for_add_playlist(self, user: User):
        return {
            "user_name": user.user_name,
            "user_password": user.user_password,
            "playlist_name": self.playlist_name
        }


class Friend(BaseModel):
    friend_name: str

    # Prepares parameters for add_friend request
    def add_friend_params(self, user : User):
        return {
            "friend_name": self.friend_name,
            "user_name": user.user_name,
            "user_password": user.user_password,
        }