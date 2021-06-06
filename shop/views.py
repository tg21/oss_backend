from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .models import user
import json
from django.core.serializers import serialize
# Create your views here.


def firstFun(request):
    return HttpResponse("You Either Die a hero, or you live long enough to see yourself become a villian")

def login(request):
    if(request.method == "POST"):
        try:
            received_json_data = json.loads(request.body.decode("utf-8"))
            u = user.objects.get(username=received_json_data.get('username'))
            if(u != None):
                if(u.isBlocked == True):
                    return JsonResponse({'auth':'blocked'})
                return JsonResponse(u._getLoginView())
            return JsonResponse({'auth':'unauthorized'})
        except Exception as e:
            return HttpResponse(str(type(e)))
    else:
        return HttpResponse("You Don't GET it. Get it?")