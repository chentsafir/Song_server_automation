from infra import http_request


CLIENT_HEADERS = {'X-Client-Type': 'song_server_automation'}


class ClientApi:
    def __init__(self, host):
        self.host = host


    # Add another user as a friend
    def add_friend(self, json_data):
        r = http_request.put(host=self.host, path="/users/add_friend", json_data=json_data, headers=CLIENT_HEADERS)
        return r

    # Add a new playlist for the user
    def add_playlist(self, json_data):
        r = http_request.post(host=self.host, path="/users/add_playlist", json_data=json_data, headers=CLIENT_HEADERS)
        return r

    # Add new user to system
    def add_user(self, json_data):
        # user.prepare_for_add_user - >מנקה את כל השדות שלא רלונטיים ליירת יוסר , רק זמנית לפני השליחה לא משפיע על קלאס עצמו (לא חייב כרגע - זה ללימוד והבנה)
        r = http_request.post(host= self.host , path= "/users/add_user" , json_data=json_data , headers=CLIENT_HEADERS)
        return r


    # Change user's password
    def change_password(self, json_data):
        r = http_request.put(host=self.host, path="/users/change_password", json_data=json_data, headers=CLIENT_HEADERS)
        return r


    # Get user's playlist
    def get_playlist(self, params=None):
        r = http_request.get(host=self.host , path="/users/get_playlist", params=params , headers=CLIENT_HEADERS )
        return r

    # Get user information
    def get_user(self, params=None):
        r = http_request.get(host=self.host , path="/users/get_user", params=params , headers=CLIENT_HEADERS)
        return r


    # Add a new song to the system
    def add_song_to_system(self, json_data):
        r = http_request.post(host=self.host, path="/songs/add_song", json_data=json_data, headers=CLIENT_HEADERS)
        return r


    # Downvote a song in system
    def downvote(self, json_data):
        r = http_request.put(host=self.host, path= "/songs/downvote", json_data=json_data, headers=CLIENT_HEADERS)
        return r


    # Get information about a specific song
    def get_song(self, params=None):
        r = http_request.get(host=self.host , path="/songs/get_song", params=params , headers=CLIENT_HEADERS)
        return r


    # Get ranked songs based on a specified rank and operator
    def get_ranked_songs(self, params=None):
        r = http_request.get(host=self.host , path="/songs/ranked_songs", params=params , headers=CLIENT_HEADERS )
        return r


    # Upvote a song in system
    def upvote(self, json_data):
        r = http_request.put(host=self.host, path= "/songs/upvote", json_data=json_data, headers=CLIENT_HEADERS)
        return r

    # Add a specific song into a specific playlist
    def add_song_to_playlist(self, json_data):
        r = http_request.post(host=self.host, path= "/playlists/add_song", json_data=json_data, headers=CLIENT_HEADERS)
        return

    # Delete all songs
    def delete_all_songs(self):
        r = http_request.delete(host=self.host , path="/admin/delete_all_songs")
        return r

    # Delete all users
    def delete_all_users(self):
        r = http_request.delete(host=self.host ,path="/admin/delete_all_users")
        return r
