class Endpoints:

    # Users endpoints
    USERS_ADD_USER = "/users/add_user"
    USERS_ADD_FRIEND = "/users/add_friend"
    USERS_ADD_PLAYLIST = "/users/add_playlist"
    USERS_CHANGE_PASSWORD = "/users/change_password"
    USERS_GET_PLAYLIST = "/users/get_playlist"
    USERS_GET_USER = "/users/get_user"

    # Songs endpoints
    SONGS_ADD_SONG = "/songs/add_song"
    SONGS_DOWNVOTE = "/songs/downvote"
    SONGS_GET_SONG = "/songs/get_song"
    SONGS_RANKED_SONGS = "/songs/ranked_songs"
    SONGS_UPVOTE = "/songs/upvote"

    # Playlists endpoints
    PLAYLISTS_ADD_SONG = "/playlists/add_song"

    #Admin endpoints
    ADMIN_DELETE_ALL_SONGS="/admin/delete_all_songs"
    ADMIN_DELETE_ALL_USERS="/admin/delete_all_users"