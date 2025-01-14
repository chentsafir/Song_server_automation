import pytest
from infra.logger import logger
from logic.song_management import Songs
from logic.user_management import User , Friend , PlayList
from tests.conftest import api


@pytest.mark.basic_test
#test add song
def test_add_song(api):
    #add new song to system
    logger.info("add new song named 505 of Arctic monkeys")
    song1=Songs(song_genre="Rock" , song_performer="arctic monkeys" , song_title="505" , song_year=2007)
    add_song1=api.add_song_to_system(json_data=song1.to_json())
    assert add_song1.status_code == 200 , f"Expected status code 200 but get {add_song1.status_code}"
    logger.info(" the status code for add 505 song is 200")

    #get song
    logger.info("get the song named 505")
    r=api.get_song(song1.prepare_get_song_params())
    assert r.status_code==200 , f"Expected status code 200 but get {r.status_code}"

    #update data and check if song is in the system.
    logger.info("check if the song named 505 added")
    actual_song=song1.update_data(r.json())
    assert actual_song.song_title == song1.song_title , f"Expecting for song title 505 but get:{actual_song.song_title} "
    logger.info("the song named 505 added")


# @pytest.mark.basic_test
# #test upvote song
# def test_upvote_song(api):
#     # add new user named chen
#     logger.info("creating new first user named chen")
#     user1 = User(user_name="chen", user_password="pass111")
#     add_user1 = api.add_user(json_data=user1.to_json())
#     assert add_user1.status_code == 200, f"Expected status code 200, but got: {add_user1.status_code}"
#     logger.info("user name chen with status code 200")
#
#     # add new song to system
#     logger.info("add new song named 505 of Arctic monkeys")
#     song1 = Songs(song_genre="Rock", song_performer="arctic monkeys", song_title="505", song_year=2007)
#     add_song1 = api.add_song_to_system(json_data=song1.to_json())
#     assert add_song1.status_code == 200, f"Expected status code 200 but get {add_song1.status_code}"
#     logger.info(" the status code for add 505 song is 200")
#
#     # add playlist to chen
#     logger.info("add playlist named vibe to chen playlists")
#     playlist1 = PlayList(playlist_name="vibe")
#     add_playlist = api.add_playlist(json_data=playlist1.prepare_for_add_playlist(user1))
#     assert add_playlist.status_code == 200, f"Expected for status code 200 but get: {add_playlist.status_code}"
#     logger.info("status code for add playlist is 200")
#
#
#
#     #upvote for song in system
#     upvote_song=api.upvote(json_data=song1.prepare_vote_request())









# @pytest.mark.xfail(reason="Bug: System not allow to add song to the system (return status code 400 and dont add the song)."
#                           " also there is bug in the get_song method, when there is no song found in the system the status code is 200  ")
# #test add song
# def test_add_song(user_logic,song_logic,playlist_logic):
#     # add song to the system
#     logger.info("add new song named 505 of Arctic monkeys")
#     add_song = song_logic.add_song(song_title="505", song_performer="Arctic Monkeys", song_genre="Rock",song_year="2007")
#     get_song = song_logic.get_song(song_title="505")
#     assert get_song.status_code == 200, "Expected status code 200"
#     print(".")  ##just to evaluate the bug
#     assert add_song.status_code == 200, f"Expected status code 200 but get {add_song.status_code}"
#     logger.info(" the song 505 of Arctic monkeys added to the system")
#
#
#
#
#
#
#
# @pytest.mark.xfail(reason="Bug: System not allow to add song to the system (return status code 400 and dont add the song)."
#                           " also there is bug in the get_song method, when there is no song found in the system the status code is 200  ") ##actualy dont check the upvote because the bug in add_song
# # 3. user upvote with wrong pass
# def test_upvote_with_wrong_pass(user_logic, song_logic, playlist_logic):
#     # add new user named chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, f"Expected status code 200 ,but get: {new_user1.status_code}"
#     logger.info("user named chen created")
#
#     #add song to the system
#     logger.info("add new song named 505 of Arctic monkeys")
#     add_song = song_logic.add_song(song_title="505", song_performer="Arctic Monkeys", song_genre="Rock",song_year="2007")
#     assert add_song.status_code == 200, f"Expected status code 200 but get {add_song.status_code}"
#     get_song=song_logic.get_song(song_title="505")
#     assert get_song.status_code==200, "Expected status code 200"
#     logger.info(" the song 505 of Arctic monkeys added to the system")
#
#     # create new playlist name vibe
#     logger.info("creating new playlist name vibe")
#     add_playlist=user_logic.add_playlist(user_name="chen", user_password="pass111", playlist_name="vibe")
#     assert add_playlist.status_code == 200, f"Expected status code 200 but get: {add_playlist.status_code} "
#     logger.info("creating new playlist name vibe succeed")
#
#     #add song to playlist
#     logger.info("add song 505 to playlist vibe")
#     add_song_to_playlist=playlist_logic.add_song(user_name="chen" , user_password= "pass111" , playlist_name="vibe" , song_title="505")
#     assert add_song_to_playlist.status_code == 200 , f"Expected status code 200 but get: {add_song_to_playlist.status_code}"
#     logger.info(" song 505 added to playlist vibe")
#
#     #upvote song with wrong pass
#     logger.info("upvote song with wrong pass")
#     upvote_song=song_logic.upvote(user_name="chen" , user_password="pass222" , playlist_name="vibe" , song_title="505")
#     assert upvote_song.status_code==400 , f"to upvote with wrong user password, status code should be 400 but get: {upvote_song.status_code} "
#     logger.info("the response status code is 400")
#     assert 'error' in upvote_song.text , "Expected User messege - password incorrect  , and not upvote , but actual upvote "  ####check it again (remove the assert status code to see th e problem)
#     logger.info("upvote to song 505 not succeed")
#
#
#
# @pytest.mark.xfail(reason="Bug: System not allow to add song to the system (return status code 400 and dont add the song).")
# # 6. user upvote twice the same song
# def test_upvote_twice_the_same_song(user_logic , song_logic ,playlist_logic):
#     # add new user named chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # add song to the system
#     logger.info("add new song named 505 of Arctic monkeys")
#     add_song = song_logic.add_song(song_title="505", song_performer="Arctic Monkeys", song_genre="Rock",
#                                    song_year="2007")
#     assert add_song.status_code == 200, f"Expected status code 200 but get {add_song.status_code}"
#     logger.info(" the song 505 of Arctic monkeys added to the system")
#
#     # create new playlist name vibe
#     logger.info("creating new playlist name vibe")
#     add_playlist = user_logic.add_playlist(user_name="chen", user_password="pass111", playlist_name="vibe")
#     assert add_playlist.status_code == 200, f"Expected status code 200 but get: {add_playlist.status_code} "
#     logger.info("creating new playlist name vibe succeed")
#
#     # add song to playlist
#     logger.info("add song 505 to playlist vibe")
#     add_song_to_playlist = playlist_logic.add_song(user_name="chen", user_password="pass111", playlist_name="vibe",
#                                                    song_title="505")
#     assert add_song_to_playlist.status_code == 200, f"Expected status code 200 but get: {add_song_to_playlist.status_code}"
#     logger.info(" song 505 added to playlist vibe")
#
#     # upvote song first time
#     logger.info("upvote song 505 by chen")
#     upvote_song = song_logic.upvote(user_name="chen", user_password="pass111", playlist_name="vibe", song_title="505")
#     assert upvote_song.status_code == 200, f"Expected status code 200 but get: {upvote_song.status_code} "
#     logger.info("the response status code is 200")
#     assert 'error' not in upvote_song.text, "Expected text - action-completed!"
#     logger.info("upvote to song 505 succeed")
#
#     # upvote song second time
#     logger.info("upvote song 505 by chen")
#     upvote_song2 = song_logic.upvote(user_name="chen", user_password="pass111", playlist_name="vibe", song_title="505")
#     assert upvote_song2.status_code == 200, f"Expected status code 200 but get: {upvote_song.status_code} "
#     logger.info("the response status code is 200")
#     assert 'error' not in upvote_song.text, "Expected text - action-completed!" ## i dont know what i suppose to get here in the second time because i cant evaluate the input (there bug in add_song)
#     logger.info("upvote to song 505 succeed")
#
#     #get song with rank 1
#     logger.info("get the song with rank 1 and check if 505 is in there")
#     get_song_rank=song_logic.get_ranked_songs(rank="1" , op="eq") ## i dont know what i suppose to get here- where is the name of the ranked song back? in json()? (there bug in add_song)
#     response_rank_song=get_song_rank.json()
#     assert "505" in response_rank_song["songs"] , "Expected that the song 505 rank is 1" ## i made it up because i dont know how the json() look like
#     logger.info("505 rank is 1")
#
#
# @pytest.mark.xfail(reason="Bug: System not allow to add song to the system (return status code 400 and dont add the song).")
# # 7. add 2 songs to the same user playlist
# def test_add_two_songs_to_playlist(user_logic,song_logic,playlist_logic):
#     # add new user named chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # add song to the system
#     logger.info("add new song named 505 of Arctic monkeys")
#     add_song = song_logic.add_song(song_title="505", song_performer="Arctic Monkeys", song_genre="Rock",
#                                    song_year="2007")
#     assert add_song.status_code == 200, f"Expected status code 200 but get {add_song.status_code}"
#     logger.info(" the song 505 of Arctic monkeys added to the system")
#
#     # add song to the system
#     logger.info("add new song named arabella of Arctic monkeys")
#     add_song2 = song_logic.add_song(song_title="arabella", song_performer="Arctic Monkeys", song_genre="Rock",
#                                    song_year="2013")
#     assert add_song2.status_code == 200, f"Expected status code 200 but get {add_song2.status_code}"
#     logger.info(" the song arabella of Arctic monkeys added to the system")
#
#     # create new playlist name vibe
#     logger.info("creating new playlist name vibe")
#     add_playlist = user_logic.add_playlist(user_name="chen", user_password="pass111", playlist_name="vibe")
#     assert add_playlist.status_code == 200, f"Expected status code 200 but get: {add_playlist.status_code} "
#     logger.info("creating new playlist name vibe succeed")
#
#     # add first song to playlist
#     logger.info("add song 505 to playlist vibe")
#     add_song_to_playlist = playlist_logic.add_song(user_name="chen", user_password="pass111", playlist_name="vibe",
#                                                    song_title="505")
#     assert add_song_to_playlist.status_code == 200, f"Expected status code 200 but get: {add_song_to_playlist.status_code}"
#     logger.info(" song 505 added to playlist vibe")
#
#     # add second song to playlist
#     logger.info("add song arabella to playlist vibe")
#     add_song2_to_playlist = playlist_logic.add_song(user_name="chen", user_password="pass111", playlist_name="vibe",
#                                                    song_title="arabella")
#     assert add_song2_to_playlist.status_code == 200, f"Expected status code 200 but get: {add_song2_to_playlist.status_code}"
#     logger.info(" song arabella added to playlist vibe")
#
#     #check that the length of playlist vibe of chen's is 2 (avi not added twice)
#     logger.info("check that the length of playlist vibe of chen's is 2")
#     get_user = user_logic.get_user("chen")
#     assert get_user.status_code == 200, "Expected status code 200"
#     response_data = get_user.json()
#     print(response_data)
#     assert 2 == len(response_data["data"]["playlists"]["vibe"]) , f"Expected that the len of vibe is 2 because we add 505 and arabella"
#     logger.info("505 and arabella is in the vibe playlist")
#
#
#
# @pytest.mark.xfail(reason="Bug: System not allow to add song to the system (return status code 400 and dont add the song).")
# # 7. add song to playlist that not exist
# def test_add_song_to_not_exist_playlist(user_logic,song_logic,playlist_logic):
#     # add new user named chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # add song to the system
#     logger.info("add new song named arabella of Arctic monkeys")
#     add_song2 = song_logic.add_song(song_title="arabella", song_performer="Arctic Monkeys", song_genre="Rock",
#                                     song_year="2013")
#     assert add_song2.status_code == 200, f"Expected status code 200 but get {add_song2.status_code}"
#     logger.info(" the song arabella of Arctic monkeys added to the system")
#
#     # add second song to playlist
#     logger.info("add song arabella to playlist vibe")
#
#     add_song2_to_playlist = playlist_logic.add_song(user_name="chen", user_password="pass111", playlist_name="vibe",
#                                                     song_title="arabella")
#     assert add_song2_to_playlist.status_code == 400, f"Expected status code 400 but get: {add_song2_to_playlist.status_code} " ##expected try and catch?
#     logger.info("There is no playlist named vibe to add the song arabella")
#
#
