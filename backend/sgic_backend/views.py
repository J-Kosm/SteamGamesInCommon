from django.http import HttpRequest, JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .services import get_user_friendslist, get_games_dict, process_shared_games_dict, get_games_from_db

@ensure_csrf_cookie
def get_friendslist(request: HttpRequest):
    if request.method == "GET":
        steam_id = request.GET.get("user_steam_id")
        
        friends_dict = get_user_friendslist(steam_id)

        return JsonResponse(friends_dict)
    else:
        return HttpResponse("Nothing...?")

def get_shared_games(request: HttpRequest):
    if request.method == "POST":
        selected_friends = request.POST.copy().getlist("selected_friends[]")
        user_steam_id = request.POST.copy().get("user_steam_id")

        # Gather a set of the user's games, and the dict for those games
        shared_games_set, shared_games_dict = get_games_dict(user_steam_id)
        
        # Get a set and dict for each of the selected friend's games,
        # then update the set of games they have in common,
        # then update the dict to only contain the shared games
        ## friend_games_dict is unused here.
        for friend in selected_friends:
            print(friend)
            friend_games_set, friend_games_dict = get_games_dict(friend)
            shared_games_set.intersection_update(friend_games_set)
            shared_games_dict = {x: shared_games_dict[x] for x in shared_games_set}
        
        # Get the tags for the shared games, if they are not already stored in the DB, and then add a record for that game into the db
        process_shared_games_dict(shared_games_dict)

        # get the shared game data from the db, and format it to be returned to frontend
        data = get_games_from_db(shared_games_set)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("Nothing...?")


