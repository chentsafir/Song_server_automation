import pytest

from infra.logger import logger

@pytest.mark.basic_test
@pytest.mark.skip(reason="this test need to be change - old test")
#add song to playlist
def test_add_song_to_playlist(api):
    # add new user named chen
    logger.info("creating new first user named chen")
    new_user1 = api.add_user(user_name="chen", user_password="pass111")
    assert new_user1.status_code == 200, f"Expected status code 200 ,but get: {new_user1.status_code}"

    logger.info("user named chen created")

    # create new playlist name vibe
    logger.info("creating new playlist name vibe")
    add_playlist = api.add_playlist(user_name="chen", user_password="pass111", playlist_name="vibe")
    assert add_playlist.status_code == 200, f"Expected status code 200 but get: {add_playlist.status_code} "
    logger.info("creating new playlist name vibe succeed")

    # add song to the system
    logger.info("add new song named 505 of Arctic monkeys")
    add_song = api.add_song(song_title="505", song_performer="Arctic Monkeys", song_genre="Rock",song_year="2007")
    assert add_song.status_code == 200, f"Expected status code 200 but get {add_song.status_code}"
    get_song = api.get_song(song_title="505")
    assert get_song.status_code == 200, "Expected status code 200"
    logger.info(" the song 505 of Arctic monkeys added to the system")

    #add song to playlist
    logger.info("add song 505 to chen's vibe platlist")
    add_song_t_playlist=api.add_song(user_name="chen" , user_password="pass111" , playlist_name="vibe" , song_title="505")
    assert add_song_t_playlist.status_code==200 , f"Expected status code 200 but get: {add_song_t_playlist.status_code}"
    get_playlist=api.get_playlist(playlist_name="vibe" , user_name="chen" , user_password="pass111")
    assert get_playlist.status_code==200 , f"Expected status code 200 but get: {get_playlist.status_code}"
    response_get_playlist=get_playlist.json()
    assert "505" in response_get_playlist , f"Expected that 505 song will be in the vibe playlist"
    logger.info("The song 505 added to vibe playlist")