import json
from infra import http_request
from logic.user_management import User, Friend, PlayList
from logic.song_management import Songs
from logic.playlist_management import PlayLists
api = http_request.HttpRequest()


# Add another user as a friend
def send_add_friend(user : User):
    r=api.put(endpoint="/users/add_friend" , data=user.to_json()  )
    return r


# Add a new playlist for the user
def add_playlist(playlist : PlayList):
    r=api.post(endpoint="/users/add_playlist" ,  data=playlist.to_json())
    return r


#Add new user to system
def send_add_user(user : User):
    # user.prepare_for_add_user - >מנקה את כל השדות שלא רלונטיים ליירת יוסר , רק זמנית לפני השליחה לא משפיע על קלאס עצמו (לא חייב כרגע - זה ללימוד והבנה)
    r = api.post(endpoint="/users/add_user",data=user.to_json())
    return r


# Change user's password
def change_password( user: User):
    r = api.put(endpoint="/users/change_password" , data=user.to_json())
    return r


# Get user's playlist
def get_playlist( user: User):
    r = api.get(endpoint="/users/get_playlist" , params=json.loads(user.to_json()))
    return r


# Get user information
def get_user( user: User):
    r = api.get(endpoint= "/users/get_user", params=user)
    return r


# Add a new song to the system
def add_song(song : Songs ):
    r = api.post(endpoint="/songs/add_song", data=song.to_json())
    return r

# Downvote a song in system
def downvote(song : Songs):
    r =api.put(endpoint="/songs/downvote", data=song.to_json())
    return r


# Get information about a specific song
def get_song(song : Songs):
    r = api.get(endpoint="/songs/get_song", params=json.loads(song.to_json()))
    return r


# Get ranked songs based on a specified rank and operator
def get_ranked_songs(song: Songs):
    r = api.get(endpoint="/songs/ranked_songs", params=json.loads(song.to_json()))
    return r


# Upvote a song in system
def upvote( song: Songs):
    r = api.put(endpoint="/songs/upvote", data=song.to_json())
    return r


# Add a specific song into a specific playlist
def add_song(playlist: PlayLists):
    r = api.post(endpoint="/playlists/add_song", data=playlist.to_json())
    return

#Delete all songs
def delete_all_songs():
    r=api.delete(endpoint="/admin/delete_all_songs")
    return r

#Delete all users
def delete_all_users():
    r=api.delete(endpoint="/admin/delete_all_users")
    return r
