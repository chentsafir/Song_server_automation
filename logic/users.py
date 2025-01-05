from logic.endpoints import Endpoints
from infra.crud_api import CrudApi

#Ask if there is need to add headers to the POST & GET

class UserLogic:


    def __init__(self):
        self.api=CrudApi()

    #Add another user as a friend
    def add_friend(self, user_name: str, user_password: str, friend_name: str):
        data = {
            "user_name": user_name,
            "user_password": user_password,
            "friend_name": friend_name
        }
        return self.api.put(Endpoints.USERS_ADD_FRIEND, data=data)


    #Add a new playlist for the user
    def add_playlist(self, user_name: str, user_password: str, playlist_name: str):
        data = {
            "user_name": user_name,
            "user_password": user_password,
            "playlist_name": playlist_name
        }
        return self.api.post(Endpoints.USERS_ADD_PLAYLIST, data=data)


    #Add a new user to the system
    def add_user(self, user_name: str, user_password: str):
        data = {
            "user_name": user_name,
            "user_password": user_password
        }
        return self.api.post(Endpoints.USERS_ADD_USER, data=data)


    #Change user's password
    def change_password(self, user_name: str, user_password: str, user_new_password: str):
        data = {
            "user_name": user_name,
            "user_password": user_password,
            "user_new_password": user_new_password
        }
        return self.api.put(Endpoints.USERS_CHANGE_PASSWORD, data=data)


    #Get user's playlist
    def get_playlist(self, user_name: str, user_password: str, playlist_name: str):
        params = {
            "user_name": user_name,
            "user_password": user_password,
            "playlist_name": playlist_name
        }
        return self.api.get(Endpoints.USERS_GET_PLAYLIST, params=params)


    #Get user information
    def get_user(self, user_name: str):
        params = {
            "user_name": user_name
        }
        return self.api.get(Endpoints.USERS_GET_USER, params=params)