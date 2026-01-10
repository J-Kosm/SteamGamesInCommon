import requests
from django.conf import settings

KEY = settings.STEAM_API_KEY


def get_friend_ids(user_id):
    request_path = f"https://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={KEY}&steamid={user_id}"
    response = requests.get(request_path)

    # don't know what this does
    response.raise_for_status()
    
    if not response:
        raise Exception(f"Failure. Status code: {response.status_code}")

    friend_ids = []
    for friend in response.json()["friendslist"]["friends"]:
        friend_ids.append(friend["steamid"])
    
    return friend_ids

def get_user_data_from_id(user_ids):
    request_path = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={KEY}&steamids={user_ids}"
    response = requests.get(request_path)
    
    # don't know what this does
    response.raise_for_status()

    if not response:
        raise Exception(f"Failure. Status code: {response.status_code}")
    # print("Successfull GET request")

    friends_dict = {}
    for player in response.json()["response"]["players"]:
        friends_dict[player["steamid"]] = {
            "username": player["personaname"],
            "avatarfull": player["avatarfull"]
            }

    return friends_dict


def get_user_friendslist(user_id):
    friend_ids = get_friend_ids(user_id)
    friends_dict = get_user_data_from_id(friend_ids)

    return friends_dict