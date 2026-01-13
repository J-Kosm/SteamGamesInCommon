from django.http import JsonResponse, HttpResponse
from django.template import loader
from .services import get_user_friendslist


def get_friendslist(request):
    if request.method == "GET":
        steam_id = request.GET.get("user_steam_id")
        
        friends_dict = get_user_friendslist(steam_id)

        return JsonResponse(friends_dict)
        # template = loader.get_template("./sgic_backend/friendslist.html")
        # context = { "friendslist" : friends_dict }
        # return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("Nothing...?")

def get_shared_games(request): 
    return HttpResponse("hiiii post")
    pass
