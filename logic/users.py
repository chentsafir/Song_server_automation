from logic.endpoints import Endpoints
from infra.crud_api import CrudApi
from logic.user_management import User, Friend
import json


# Ask if there is need to add headers to the POST & GET

class UserLogic:

    def __init__(self):
        self.api = CrudApi()

    # Add another user as a friend
    def add_friend(self,  data = Friend):

        return self.api.put(Endpoints.USERS_ADD_FRIEND, data=data.to_json())

    # Add a new playlist for the user
    def add_playlist(self, user_data: User):
        r= self.api.post(Endpoints.USERS_ADD_PLAYLIST, data=user_data.to_json())
        return r



    # Add a new user to the system
    def add_user(self, user_data: User):
        response = self.api.post(Endpoints.USERS_ADD_USER, data=user_data.to_json())

        return response



    # Change user's password
    def change_password(self, user_data: User):
        r=self.api.put(Endpoints.USERS_CHANGE_PASSWORD, data=user_data.to_json())
        return r


    # Get user's playlist
    def get_playlist(self, user_data : User):
        r=self.api.get(Endpoints.USERS_GET_PLAYLIST, params=json.loads(user_data.to_json()))
        return r


    # Get user information
    def get_user(self, user : User):
        r=self.api.get(Endpoints.USERS_GET_USER, params=USER_NAME)

        return r
