import requests
import json
from bs4 import BeautifulSoup
from django.conf import settings
from django.core import serializers
from .models import Game

KEY = settings.STEAM_API_KEY


def get_friend_ids(user_id):
    request_path = f"https://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={KEY}&steamid={user_id}"
    response = requests.get(request_path)

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
    
    response.raise_for_status()

    if not response:
        raise Exception(f"Failure. Status code: {response.status_code}")
    # print("Successfull GET request")

    friends_dict = {}
    for player in response.json()["response"]["players"]:
        friends_dict[player["steamid"]] = {
            "steam_id": player["steamid"],
            "username": player["personaname"],
            "avatarfull": player["avatarfull"]
            }

    return friends_dict


def get_user_friendslist(user_id):
    friend_ids = get_friend_ids(user_id)
    friends_dict = get_user_data_from_id(friend_ids)

    return friends_dict


def get_game_tags(appid):
    request_path = f"https://store.steampowered.com/app/{appid}/"

    response = requests.get(request_path)
    response.raise_for_status()
    if not response:
        raise Exception(f"Failure. Status code: {response.status_code}")
    
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    tag_elements = soup.find_all('a', class_="app_tag")

    app_tags = []
    for app in tag_elements:
        app_tags.append(app.get_text(strip=True))

    return app_tags


def get_games_dict(user_id):
    request_path = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={KEY}&steamid={user_id}&include_appinfo=true"
    response = requests.get(request_path)
    response.raise_for_status()
    if not response:
        raise Exception(f"Failure. Status code: {response.status_code}")

    owned_games_set = set()
    owned_games_dict = {}

    try:
        data = response.json()["response"]["games"]
        for game in data:
            owned_games_set.add(game["appid"])
            owned_games_dict[game["appid"]] = {
                "name": game["name"],
                "img_icon_url": game["img_icon_url"]
            }
    except:
        print(f"User {user_id} had no games or is set to private.")
    
    return owned_games_set, owned_games_dict


def process_shared_games_dict(shared_games_dict: dict):
    for game in shared_games_dict:
        if not Game.objects.filter(appid=game).exists(): 
            # print debug
            print(f"New game: {shared_games_dict[game]["name"]}")

            game_tags = get_game_tags(game)
            game = Game(appid=game, name=shared_games_dict[game]["name"], img_icon_url=shared_games_dict[game]["img_icon_url"], tags=game_tags)
            game.save()
        else:
            # print debug
            print(f"Old game: {shared_games_dict[game]["name"]}")


def get_games_from_db(games_set: set):
    queryset = Game.objects.filter(appid__in=games_set).values("appid", "name", "img_icon_url", "tags")
    data = list(queryset)
    
    return data


# from a list of users, get only their multiplayer games, and then return only those which they have in common.
def get_shared_multiplayer_games():
    return 