import re
from infra.logger import logger
import pytest
from logic.user_management import User , PlayList , Friend



@pytest.mark.basic_test
# test add user
def test_add_user(api):
    # add new user named chen
    logger.info("creating new first user named chen")
    user1 = User(user_name="chen", user_password="pass111")
    add_user1 = api.add_user(json_data=user1.to_json())
    assert add_user1.status_code == 200, f"Expected status code 200, but got: {add_user1.status_code}"
    logger.info("user name chen with status code 200")

    # get user named chen data
    logger.info("get chen details")
    r2 = api.get_user(user1.convert_username_to_params_dict())
    # r2 = api.get_user({'user_name' : user1.user_name}) ## there is another option but i didnt know if its good so i create function in user_management that return the name in dict
    assert r2.status_code == 200, f"Expected for status code 200 but get: {r2.status_code}"
    actual_user=user1.update_data(r2.json())
    assert actual_user.user_name == user1.user_name , "Every new user should have user name"
    # assert actual_user.user_password == user1.user_new_password, "Every new user should have password"
    assert actual_user.friend_list == [] , "Every new user should have empty list of friend"
    assert actual_user.friend_list == [], "Every new user should have empty list of playlist"
    logger.info("user named chen is added")


@pytest.mark.basic_test
# test add playlist
def test_add_playlist(api):
    # add new user named chen
    logger.info("creating new first user named chen")
    user1 = User(user_name="chen", user_password="pass111")
    add_user1 = api.add_user(json_data=user1.to_json())
    assert add_user1.status_code == 200, f"Expected status code 200, but got: {add_user1.status_code}"
    logger.info("user name chen with status code 200")

    # add playlist to chen
    logger.info("add playlist named vibe to chen playlists")
    playlist1=PlayList(playlist_name="vibe")
    add_playlist = api.add_playlist(json_data=playlist1.prepare_for_add_playlist(user1))
    assert add_playlist.status_code == 200, f"Expected for status code 200 but get: {add_playlist.status_code}"
    logger.info("status code for add playlist is 200")

    # get user named chen data
    logger.info("get chen details")
    r2 = api.get_user(user1.convert_username_to_params_dict())
    # r2 = api.get_user({'user_name' : user1.user_name}) ## there is another option but i didnt know if its good so i create function in user_management that return the name in dict
    assert r2.status_code == 200, f"Expected for status code 200 but get: {r2.status_code}"
    actual_user = user1.update_data(r2.json())
    assert playlist1 in actual_user.playlist_list
    logger.info("playlist named vibe add to chen's playlists")



@pytest.mark.basic_test
@pytest.mark.parametrize("user_data,friend_data" ,[
                         (
                            {"name" : "chen" , "password" : "pass111"},
                            {"name" : "adam" , "password" : "pass222"}
                         ),
                         (
                            {"name": "ron", "password": "pass333"},
                            {"name": "elad", "password": "pass444"}
                         ),
                         (
                            {"name": "dani", "password": "pass555"},
                            {"name": "tomer", "password": "pass666"}
                         )
])
# test add friend
def test_add_friend(api , user_data , friend_data):
    # add new first user1
    logger.info(f"creating new first user named {user_data['name']}")
    user1 = User(user_name=user_data["name"], user_password=user_data["password"])
    add_user1 = api.add_user(json_data=user1.to_json())
    assert add_user1.status_code == 200, f"Expected status code 200, but got: {add_user1.status_code}"
    logger.info(f"user name  {user_data['name']} with status code 200")

    # add new second user2
    logger.info(f"creating new second user named {friend_data["name"]}")
    user2 = User(user_name=friend_data["name"], user_password=friend_data["password"])
    add_user2 = api.add_user(json_data=user2.to_json())
    assert add_user2.status_code == 200, f"Expected status code 200 but get: {add_user2.status_code}"
    logger.info(f"user named {friend_data["name"]} created")

    # add friend
    logger.info(f"add {friend_data["name"]} to {user_data['name']}'s friends")
    friend1=Friend(friend_name=user2.user_name)
    add_friend = api.add_friend(json_data=friend1.add_friend_params(user1))
    assert add_friend.status_code == 200, f"Expected status code 200 but get: {add_friend.status_code}"
    logger.info("status code 200 for add friend")

    # get user1 data
    logger.info(f"get {user_data['name']} details")
    r2 = api.get_user(user1.convert_username_to_params_dict())
    assert r2.status_code == 200, f"Expected for status code 200 but get: {r2.status_code}"
    actual_user = user1.update_data(r2.json())
    assert friend1 in actual_user.friend_list
    logger.info(f"friend named {friend_data["name"]} added to {user_data['name']}'s friends")



@pytest.mark.basic_test
def test_change_password(api):
    # add new user named chen
    logger.info("creating new user named chen")
    user1 = User(user_name="chen", user_password="pass111")
    add_user1 = api.add_user(json_data=user1.to_json())
    assert add_user1.status_code == 200, f"Expected status code 200, but got: {add_user1.status_code}"
    logger.info("user chen created successfully")

    # change password
    logger.info("changing password for user chen")
    user1.user_new_password = "pass222"  # Set the new password
    change_password = api.change_password(json_data=user1.prepare_change_password_request())
    assert change_password.status_code == 200, f"Expected status code 200, but got: {change_password.status_code}"
    logger.info("password changed successfully")

    # Update the user object with the new password
    user1.update_password()

    # Check if password changed. with an action with the new password
    logger.info("check if password changed by adding a playlist")
    playlist1 = PlayList(playlist_name="vibe")
    add_playlist = api.add_playlist(json_data=playlist1.prepare_for_add_playlist(user1))
    assert add_playlist.status_code == 200, f"Expected status code 200, but got: {add_playlist.status_code}"
    logger.info("password changed to new password")


@pytest.mark.xfail(run=True , reason= "bug - add user with the same name and system not case sensitive")
@pytest.mark.Tests_according_to_requirements
@pytest.mark.parametrize ("user_data1,user_data2" , [
    (
        {"name": "chen", "password": "pass111"} ,
        {"name": "chen", "password": "pass111"}
    ),
    (
        {"name": "chen", "password": "pass222"} ,
        {"name": "Chen", "password": "pass222"}
    )
] )
# 1. add 2 users with the same name (also check if the system is CaseSensitive) use parametrize
def test_add_2_users_with_the_same_name(api , user_data1 , user_data2 ):
    # add new user named chen
    logger.info(f"creating new first user named {user_data1["name"]}")
    user1 = User(user_name=user_data1["name"], user_password=user_data1["password"])
    add_user1 = api.add_user(json_data=user1.to_json())
    assert add_user1.status_code == 200, f"Expected status code 200, but got: {add_user1.status_code}"
    logger.info(f"user name {user_data1["name"]} with status code 200")

    # get user named chen data
    logger.info(f"get {user_data1["name"]} details")
    r2 = api.get_user(user1.convert_username_to_params_dict())
    # r2 = api.get_user({'user_name' : user1.user_name}) ## there is another option but i didnt know if its good so i create function in user_management that return the name in dict
    assert r2.status_code == 200, f"Expected for status code 200 but get: {r2.status_code}"
    actual_user=user1.update_data(r2.json())
    assert actual_user.user_name == user1.user_name
    logger.info(f"user named {user_data1["name"]} is added")

    # add new second user named chen
    logger.info(f"creating new second user named {user_data2["name"]}")
    user1 = User(user_name=user_data2["name"], user_password=user_data2["password"])
    add_user1 = api.add_user(json_data=user1.to_json())
    assert add_user1.status_code != 200, f"Expected status code different from 200, but got: {add_user1.status_code}"
    logger.info(f"user name {user_data2["name"]} with status code 200")

    # get user named chen data
    logger.info(f"get {user_data2["name"]} details")
    r2 = api.get_user(user1.convert_username_to_params_dict())
    # r2 = api.get_user({'user_name' : user1.user_name}) ## there is another option but i didnt know if its good so i create function in user_management that return the name in dict
    assert r2.status_code != 200, f"Expected for status code different from 200 but get: {r2.status_code}"
    actual_user=user1.update_data(r2.json())
    assert actual_user.user_name == user1.user_name
    logger.info(f"user named {user_data2["name"]} is added")




@pytest.mark.xfail(run=True , reason= "bug - add user with empty name \ Invalid characters name")
@pytest.mark.Tests_according_to_requirements
@pytest.mark.parametrize ("user_data1" , [
    (
        {"name": "   ", "password": "pass111"}
    ),
    (
        {"name": "!!!", "password": "pass222"}
    ),
    (
        {"name": "@@@", "password": "pass333"}
    )
] )
#2. every new user in the system has name (check if create user with empty name \ Invalid characters name  is valid)
def test_user_has_name(api , user_data1):
    # add new user with no name (@@@/!!!/  /"")
    logger.info(f"creating new first user named {user_data1["name"]}")
    user1 = User(user_name=user_data1["name"], user_password=user_data1["password"])
    add_user1 = api.add_user(json_data=user1.to_json())
    assert add_user1.status_code != 200, f"Expected status code different from 200, but got: {add_user1.status_code}"
    logger.info(f"name {user_data1["name"]} with status code different from 200")

    # get user1 data
    logger.info(f"get {user_data1['name']} details to check if not added to system")
    r2 = api.get_user(user1.convert_username_to_params_dict())
    assert r2.status_code != 200, f"Expected for status code different from 200 but get: {r2.status_code}"
    actual_user = user1.update_data(r2.json())
    assert user_data1["name"] not in actual_user.user_name
    logger.info(f" user {user_data1['name']} is not added to the system")


#
#
# # TODO
# @pytest.mark.xfail(reason="Bug: System allows add empty usernames")
# # 2. every new user in the system has name (check if i create user with empty name is valid)
# def test_user_has_name(user_logic):
#     logger.info("Starting test: user_has_name")
#
#     # add new user with empty named
#     logger.info("creating new first user with empty name")
#     new_user1 = user_logic.add_user(user_name="", user_password="pass111")
#     assert new_user1.status_code == 400, f"Expected status code 400 but get: {new_user1.status_code}"
#     logger.info("user without name not created")
#
#     # get user with empty name
#     logger.info("get chen detail")
#     get_user = user_logic.get_user(user_name="")
#     assert get_user.status_code == 400, "Expected status code 400"
#     logger.info("there is not user with empty name")
#
#
# # 2. every new user in the system has emty list of friends
# def test_user_has_friends_list(user_logic):
#     logger.info("Starting test: test_user_has_friends_list")
#
#     # add new user named chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # get user name chen
#     logger.info("get chen detail")
#     get_user = user_logic.get_user(user_name="chen")
#     assert get_user.status_code == 200, "Expected status code 200"
#     logger.info("user detail is responded")
#
#     # check that chen has emthy friends list
#     logger.info("check if user has empty list of friends")
#     response_data = get_user.json()
#     friends_response = response_data["data"]["friends"]
#     assert not friends_response, "Expected to be empty list of friends."  ## "Falsy" value in python , [] , ("") , 0 , None
#     logger.info("the user chen has empty list of friends")
#
#
# # 2. every new user in the system has emty list of playlists
# def test_user_has_playlists_list(user_logic):
#     logger.info("Starting test: test_user_has_playlists_list")
#
#     # add new user named chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # add new user name chen
#     logger.info("get chen detail")
#     get_user = user_logic.get_user(user_name="chen")
#     assert get_user.status_code == 200, "Expected status code 200"
#     logger.info("user detail is responded")
#
#     # check that chen has emthy friends list
#     logger.info("check if user has empty list of playlists")
#     response_data = get_user.json()
#     response_playlists = response_data["data"]["playlists"]
#     assert not response_playlists, "Expected to be empty list of playlists."
#     logger.info("the user chen has empty list of playlists")
#
#
# @pytest.mark.xfail(
#     reason="Bug: System not allow to add playlist with wrong password but status code is 200 instead 500 ")
# # 3. user add playlist with wrong pass
# def test_add_play_list_with_wrong_pass(user_logic):
#     # add new user named chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # create new playlist name vibe with wrong pass
#     logger.info("creating new playlist name vibe")
#     add_playlist = user_logic.add_playlist(user_name="chen", user_password="pass222", playlist_name="vibe")
#     assert add_playlist.status_code == 500, f"to add playlist with wrong user password status code should be 500 but get: {add_playlist.status_code} "
#     logger.info("creating new playlist name vibe not succeed")
#     assert 'error' in add_playlist.text, "Expected User messege - password incorrect  , and not add vibe to chen's playlists , but actual added"
#
#
# @pytest.mark.xfail(reason="Bug: System not allow to add friend with wrong password but status code is 200 instead 500 ")
# # 3. user add friend with wrong pass
# def test_add_friend_with_wrong_pass(user_logic):
#     # add new user named chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # add new user name avi
#     logger.info("creating new second user named avi")
#     new_user2 = user_logic.add_user(user_name="avi", user_password="pass222")
#     assert new_user2.status_code == 200, "Expected status code 200"
#     logger.info("user named avi created")
#
#     ## add new friend with wrong password
#     logger.info("try to add avi to chen's friends with wrong pass")
#     add_friend = user_logic.add_friend(user_name="chen", user_password="pass222", friend_name="avi")
#     assert not re.match(r"^2\d{2}$",
#                         str(add_friend.status_code)), f"to add friend with wrong user password status code should be 500 but get: {add_friend.status_code} "
#     # assert add_friend.status_code ==500, f"to add friend with wrong user password status code should be 500 but get: {add_friend.status_code} "
#     logger.info("the response status code is 500")  ##why 500 and not 400?
#     assert 'error' in add_friend.text, "Expected User messege - password incorrect  , and not add avi to chen's friend , but actual added "  ####check it again (remove the assert status code to see th e problem)
#     logger.info("avi not added to chen's friends")
#
#
# # 4. add 2 friends to the same user friends lists
# def test_add_two_friends(user_logic):
#     logger.info("Starting test: test_add_friend")
#
#     # add new user name chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # add new user name avi
#     logger.info("creating new second user named avi")
#     new_user2 = user_logic.add_user(user_name="avi", user_password="pass222")
#     assert new_user2.status_code == 200, "Expected status code 200"
#     logger.info("user named avi created")
#
#     # add new user name joe
#     logger.info("creating new third user named joe")
#     new_user3 = user_logic.add_user(user_name="joe", user_password="pass333")
#     assert new_user3.status_code == 200, "Expected status code 200"
#     logger.info("user named joe created")
#
#     # add avi to chens friends
#     logger.info("add avi to chen's friends")
#     add_freind = user_logic.add_friend(friend_name="avi", user_name="chen", user_password="pass111")
#     assert add_freind.status_code == 200, "Expected status code 200"
#     logger.info("avi added to chen's friends")
#
#     # check that avi is in chen friends
#     logger.info("check if avi is in chen's friends")
#     get_user = user_logic.get_user("chen")
#     assert get_user.status_code == 200, "Expected status code 200"
#     response_data = get_user.json()
#     print(response_data)
#     assert "avi" in response_data["data"]["friends"]
#     logger.info("avi is in chen's friends")
#
#     # add joe to chens friends
#     logger.info("add joe to chen's friends")
#     add_freind2 = user_logic.add_friend(friend_name="joe", user_name="chen", user_password="pass111")
#     assert add_freind2.status_code == 200, "Expected status code 200"
#     logger.info("joe added to chen's friends")
#
#     # check that joe is in chen friends
#     logger.info("check if joe is in chen's friends")
#     get_user = user_logic.get_user("chen")
#     assert get_user.status_code == 200, "Expected status code 200"
#     response_data = get_user.json()
#     print(response_data)
#     assert "joe" in response_data["data"]["friends"]
#     logger.info("joe is in chen's friends")
#
#
# # 4. add the same friend to chen's friends list
# def test_add_the_same_friend(user_logic):
#     # add new user name chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # add new user name avi
#     logger.info("creating new second user named avi")
#     new_user2 = user_logic.add_user(user_name="avi", user_password="pass222")
#     assert new_user2.status_code == 200, "Expected status code 200"
#     logger.info("user named avi created")
#
#     # add avi to chens friends
#     logger.info("add avi to chen's friends")
#     add_freind = user_logic.add_friend(friend_name="avi", user_name="chen", user_password="pass111")
#     assert add_freind.status_code == 200, "Expected status code 200"
#     logger.info("avi added to chen's friends")
#
#     # add avi to chens friends again
#     logger.info("add avi to chen's friends")
#     add_freind1 = user_logic.add_friend(friend_name="avi", user_name="chen", user_password="pass111")
#     assert add_freind1.status_code == 200, f"Expected status code 200 but actual get {add_freind1.status_code}"
#     logger.info("avi added to chen's friends")
#
#     # check that the length of friends lists of chen's is 1 (avi not added twice)
#     logger.info("check if the length of friends lists of chen's is 1")
#     get_user = user_logic.get_user("chen")
#     assert get_user.status_code == 200, "Expected status code 200"
#     response_data = get_user.json()
#     print(response_data)
#     assert 1 == len(response_data["data"]["friends"])
#     logger.info("avi added once")
#
#
# # 5. create 2 playlists to the same user
# def test_add_two_playlist_to_user(user_logic, song_logic, playlist_logic):
#     # add new user name chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # create new playlist name vibe
#     logger.info("creating new playlist name vibe")
#     add_playlist = user_logic.add_playlist(user_name="chen", user_password="pass111", playlist_name="vibe")
#     assert add_playlist.status_code == 200, f"Expected status code 200 but get: {add_playlist.status_code} "
#     logger.info("creating new playlist name vibe succeed")
#
#     # create new playlist name vibe
#     logger.info("creating new playlist name chill")
#     add_playlist2 = user_logic.add_playlist(user_name="chen", user_password="pass111", playlist_name="chill")
#     assert add_playlist2.status_code == 200, f"Expected status code 200 but get: {add_playlist2.status_code} "
#     logger.info("creating new playlist name chill succeed")
#
#     # check that vibe and chill is in the playlists list
#     logger.info("get chen details and check if vibe and chill is in the playlists list ")
#     get_user = user_logic.get_user(user_name="chen")
#     assert get_user.status_code == 200, f"Expected status code 200 but get: {get_user.status_code} "
#     response_data = get_user.json()
#     assert "chill" in response_data["data"]["playlists"], "Ecpected chill is in chen's playlists , but it isn't"
#     logger.info("chill is in chen's playlists")
#     assert "vibe" in response_data["data"]["playlists"], "Ecpected vibe is in chen's playlists , but it isn't"
#     logger.info("vibe is in chen's playlists")
#
#
# # 10. the password of user not return in the user data
# def test_user_data_is_safe(user_logic, song_logic, playlist_logic):
#     # add new user name chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # get user data and check if the password is return in the data response
#     logger.info("check the response from get user")
#     get_user = user_logic.get_user(user_name="chen")
#     assert get_user.status_code == 200, "Expected status code 200"
#     response_data = get_user.json()
#     assert "password" not in response_data[
#         "data"].keys(), "Expected that the password dont show in the user data return from server"
#     logger.info("The password dont show in the user data return from server")
#
#
# # 11. the user can change pass and the new pass is updates in system
# def test_user_change_pass(user_logic, song_logic, playlist_logic):
#     # add new user name chen
#     logger.info("creating new first user named chen")
#     new_user1 = user_logic.add_user(user_name="chen", user_password="pass111")
#     assert new_user1.status_code == 200, "Expected status code 200"
#     logger.info("user named chen created")
#
#     # user change pass
#     logger.info("user chen want to change password")
#     change_pass = user_logic.change_password(user_name="chen", user_password="pass111", user_new_password="pass222")
#     assert change_pass.status_code == 200, f"Expected status code 200 but get: {change_pass.status_code}"
#     logger.info("status code for change pass is 200")
#     assert "erorr" not in change_pass.text, "Expected to action complit!, but get error"
#
#     # do action that require pass and check if it done with the new pass
#     logger.info("try to add playlist named vibe to chen playlists with the new pass")
#     add_playlist = user_logic.add_playlist(user_name="chen", user_password="pass222", playlist_name="vibe")
#     assert add_playlist.status_code == 200, f"Expected status code 200 but get: {add_playlist.status_code}"
#     logger.info("status code for add playlist with new pass is 200")
#
#     # check if the vibe playlist is in the response data from server
#     logger.info("check if the vibe playlist is in the response user data from server")
#     get_user = user_logic.get_user("chen")
#     response_user_data = get_user.json()
#     assert "vibe" in response_user_data["data"]["playlists"]
#     logger.info(
#         "vibe add to the playlist so the new pass is update in the system")  ## i think that we also need to check that the old pass is not active for the user. do i need to do it?
