import re

from logic.users import UserLogic
from logic.songs import SongLogic
from logic.playlists import PlaylistLogic
from infra.logger import logger
import pytest
import logging

from tests.conftest import song_logic


# test add user (icd test)
def test_add_user(user_logic):
    # to-do
    logger.info("creating new user")
    actual_response = user_logic.add_user(user_name="chen", user_password="pass111")
    actual_data = actual_response.request.body
    # expected
    expected_user_name = "chen"
    expected_password = "pass111"
    # result
    assert actual_response.status_code == 200, "Expected status code 200"
    assert actual_response.json()["data"] == expected_user_name, f"Expected user name {expected_user_name} "
    assert actual_response.json()["message"] == "OK" "Expected OK messege"


@pytest.mark.xfail(reason="Bug: System allows duplicate usernames")
# 1. add 2 users with the same name (functional test)
def test_add_2_users_with_the_same_name(user_logic):
    logger.info("Starting test: test_add_2_users_with_the_same_name")

    # add new user named chen
    logger.info("creating new first user named chen")
    new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
    assert new_user1.status_code == 200, "Expected status code 200"
    logger.info("user named chen created")

    # add second new user named chen
    logger.info("creating new second user named chen")
    new_user2 = user_logic.add_user(user_name="chen", user_password="pass111")
    assert new_user2.status_code == 500, "Expected status code 500"
    logger.info("user named chen created")


@pytest.mark.xfail(reason="Bug: System allows duplicate usernames (the system is not case sensitive")
# 1. add 2 users with the same name but the first name is in capital letters and second in lowercase (functional test)
def test_add_2_users_with_the_same_name_case_sensitive(user_logic):
    logger.info("Starting test: test_add_2_users_with_the_same_name_case_sensitive")

    # add first new user named Chen
    logger.info("creating new first user named Chen")
    new_user1 = user_logic.add_user(user_name="Chen", user_password="pass111")
    assert new_user1.status_code == 200, "Expected status code 200"
    logger.info("user named Chen created")

    # add second new user named chen
    logger.info("creating new second user named chen")
    new_user2 = user_logic.add_user(user_name="chen", user_password="pass111")
    assert new_user2.status_code == 500, "Expected status code 500"
    logger.info("user named chen created")


# 2. every new user in the system has name
def test_user_has_name(user_logic):
    logger.info("Starting test: user_has_name")

    # add new user named chen
    logger.info("creating new first user named chen")
    new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
    assert new_user1.status_code == 200, "Expected status code 200"
    logger.info("user named chen created")

    # add new user name chen
    logger.info("get chen detail")
    get_user = user_logic.get_user(user_name="chen")
    assert get_user.status_code == 200, "Expected status code 200"
    logger.info("user detail is responded")

    # check that the name of chen in system is chen
    logger.info("check if user has name")
    response_data = get_user.json()
    expected_user_name = "chen"
    assert expected_user_name == response_data["data"]["user_name"], f"Expected user name {expected_user_name}  "
    logger.info("the user chen has name (chen)")


# 2. every new user in the system has emty list of friends
def test_user_has_friends_list(user_logic):
    logger.info("Starting test: test_user_has_friends_list")

    # add new user named chen
    logger.info("creating new first user named chen")
    new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
    assert new_user1.status_code == 200, "Expected status code 200"
    logger.info("user named chen created")

    # add new user name chen
    logger.info("get chen detail")
    get_user = user_logic.get_user(user_name="chen")
    assert get_user.status_code == 200, "Expected status code 200"
    logger.info("user detail is responded")

    # check that chen has emthy friends list
    logger.info("check if user has empty list of friends")
    response_data = get_user.json()
    friends_response = response_data["data"]["friends"]
    assert not friends_response, "Expected to be empty list of friends."  ## "Falsy" value in python , [] , ("") , 0 , None
    logger.info("the user chen has empty list of friends")


# 2. every new user in the system has emty list of playlists
def test_user_has_playlists_list(user_logic):
    logger.info("Starting test: test_user_has_playlists_list")

    # add new user named chen
    logger.info("creating new first user named chen")
    new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
    assert new_user1.status_code == 200, "Expected status code 200"
    logger.info("user named chen created")

    # add new user name chen
    logger.info("get chen detail")
    get_user = user_logic.get_user(user_name="chen")
    assert get_user.status_code == 200, "Expected status code 200"
    logger.info("user detail is responded")

    # check that chen has emthy friends list
    logger.info("check if user has empty list of playlists")
    response_data = get_user.json()
    response_playlists = response_data["data"]["playlists"]
    assert not response_playlists, "Expected to be empty list of playlists."
    logger.info("the user chen has empty list of playlists")


@pytest.mark.xfail(
    reason="Bug: System not allow to add playlist with wrong password but status code is 200 instead 500 ")
# 3. user add playlist with wrong pass
def test_add_play_list_with_wrong_pass(user_logic):
    # add new user named chen
    logger.info("creating new first user named chen")
    new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
    assert new_user1.status_code == 200, "Expected status code 200"
    logger.info("user named chen created")

    # create new playlist name vibe with wrong pass
    logger.info("creating new playlist name vibe")
    add_playlist = user_logic.add_playlist(user_name="chen", user_password="pass222", playlist_name="vibe")
    assert add_playlist.status_code == 500, f"to add playlist with wrong user password status code should be 500 but get: {add_playlist.status_code} "
    logger.info("creating new playlist name vibe not succeed")
    assert 'error' in add_playlist.text, "Expected User messege - password incorrect  , and not add vibe to chen's playlists , but actual added"


@pytest.mark.xfail(reason="Bug: System not allow to add friend with wrong password but status code is 200 instead 500 ")
# 3. user add friend with wrong pass
def test_add_friend_with_wrong_pass(user_logic):
    # add new user named chen
    logger.info("creating new first user named chen")
    new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
    assert new_user1.status_code == 200, "Expected status code 200"
    logger.info("user named chen created")

    # add new user name avi
    logger.info("creating new second user named avi")
    new_user2 = user_logic.add_user(user_name="avi", user_password="pass222")
    assert new_user2.status_code == 200, "Expected status code 200"
    logger.info("user named avi created")

    ## add new friend with wrong password
    logger.info("try to add avi to chen's friends with wrong pass")
    add_friend = user_logic.add_friend(user_name="chen", user_password="pass222", friend_name="avi")
    assert not re.match(r"^2\d{2}$",
                        str(add_friend.status_code)), f"to add friend with wrong user password status code should be 500 but get: {add_friend.status_code} "
    # assert add_friend.status_code ==500, f"to add friend with wrong user password status code should be 500 but get: {add_friend.status_code} "
    logger.info("avi not added to chen's friends")
    assert 'error' in add_friend.text, "Expected User messege - password incorrect  , and not add avi to chen's friend , but actual added "  ####check it again (remove the assert status code to see th e problem)
    logger.info("avi not added to chen's friends")


# 3. user upvote with wrong pass
def test_upvote_with_wrong_pass(user_logic, song_logic, playlist_logic):
    # add new user named chen
    logger.info("creating new first user named chen")
    new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
    assert new_user1.status_code == 200, "Expected status code 200"
    logger.info("user named chen created")

    add_song = song_logic.add_song(song_title="505", song_performer="Arctic Monkeys", song_genre="Rock",
                                   song_year="2007")


########################


# 4. add 2 friends to the same user friends (functional test)
def test_add_friend(user_logic):
    logger.info("Starting test: test_add_friend")

    # add new user name chen
    logger.info("creating new first user named chen")
    new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
    assert new_user1.status_code == 200
    logger.info("user named chen created")

    # add new user name avi
    logger.info("creating new second user named avi")
    new_user2 = user_logic.add_user(user_name="avi", user_password="pass222")
    assert new_user2.status_code == 200
    logger.info("user named avi created")

    # add avi to chens friends
    logger.info("add avi to chen's friends")
    add_freind = user_logic.add_friend(friend_name="avi", user_name="chen", user_password="pass111")
    assert add_freind.status_code == 200
    logger.info("avi added to chen's friends")

    # check that avi is in chen friends
    logger.info("check if avi is in chen's friends")
    get_user = user_logic.get_user("chen")
    assert get_user.status_code == 200
    response_data = get_user.json()
    print(response_data)
    assert "avi" in response_data["data"]["friends"]
    logger.info("avi is in chen's friends")
