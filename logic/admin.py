from logic.endpoints import Endpoints
from infra.crud_api import CrudApi


class AdminLogic:
    def __init__(self):
        self.api = CrudApi()

    def delete_all_songs(self):
        return self.api.delete(Endpoints.ADMIN_DELETE_ALL_SONGS)

    def delete_all_users(self):
        return self.api.delete(Endpoints.ADMIN_DELETE_ALL_USERS)