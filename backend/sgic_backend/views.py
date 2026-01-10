from django.http import JsonResponse, HttpResponse
from django.template import loader
from .services import get_user_friendslist


def get_friendslist(request):
    if request.method == "GET":
        steam_id = request.GET.get("steam_id")
        
        friendslist = get_user_friendslist(steam_id)

        template = loader.get_template("./sgic_backend/friendslist.html")
        context = { "friendslist" : friendslist }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("Nothing...?")


