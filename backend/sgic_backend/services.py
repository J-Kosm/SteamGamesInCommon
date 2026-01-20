import requests
import json
from bs4 import BeautifulSoup
from django.conf import settings
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

def check_if_game_in_db(appid):
    game_exists = False

    


    return game_exists

def get_owned_games(user_id):
    request_path = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={KEY}&steamid={user_id}&include_appinfo=true"

    response = requests.get(request_path)
    response.raise_for_status()
    if not response:
        raise Exception(f"Failure. Status code: {response.status_code}")
    
    data = response.json()["response"]["games"]

    owned_games_dict = {}
    new_count = 0
    stored_count = 0
    for game in data:
        owned_games_dict[game["appid"]] = {
            "name": game["name"],
            "img_icon_url": game["img_icon_url"]
        }

        
        # check if game is in db already
        if not Game.objects.filter(appid=game["appid"]).exists():
            print("New Game")
            print(game["name"])
            game_tags = get_game_tags(game["appid"])
            game = Game(appid=game["appid"], name=game["name"], img_icon_url=game["img_icon_url"], tags=game_tags)
            game.save()
            new_count += 1

        # If game is already present in db...
        else:
            # game = Game.objects.filter(game["appid"])
            print("Game present")
            print(game["name"])
            stored_count +=1
        
        
    print(f"New games: {new_count}")
    print(f"Games already stored: {stored_count}")

        

    return owned_games_dict
    




def add_game_to_db(appid):

    return None