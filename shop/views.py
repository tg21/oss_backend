from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .models import user
import json
# Create your views here.


def firstFun(request):
    return HttpResponse("You Either Die a hero, or you live long enough to see yourself become a villian")

def login(request):
    if(request.method == "POST"):
        try:
            received_json_data = json.loads(request.body.decode("utf-8"))
            u = user.Objects.get(first_name=received_json_data.emailId)
            if(u != None):
                return JsonResponse({'data':'authorized'})
            return JsonResponse({'data':'unauthorized'})
        except Exception as e:
            return HttpResponse(str(type(e)))
    else:
        return HttpResponse("You Don't GET it. Get it?")