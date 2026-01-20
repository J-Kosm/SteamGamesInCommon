from django.http import HttpRequest, JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .services import get_user_friendslist, get_owned_games, get_game_tags

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

        result = get_owned_games(selected_friends[0])

        
        

        return JsonResponse(selected_friends, safe=False)
    else:
        return HttpResponse("Nothing...?")


