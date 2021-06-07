from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .models import user,category,item
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
            return HttpResponse(str(type(e)),status=500)
    else:
        return HttpResponse("You Don't GET it. Get it?",status=400)

def getCategories(request):
    try:
        # c = serialize('json',list(category.objects.filter().values('category')))
        c = list(category.objects.all().values('id','category'))
        return JsonResponse(c,safe=False)
    except Exception as e:
            return HttpResponse(str(type(e)),status=500)

def getItemsForCategory(request,categoryId:int):
    try:
        c = list(item.objects.filter(category_id = categoryId).values())
        return JsonResponse(c,safe=False)
    except Exception as e:
        return HttpResponse(str(type(e)),status=500)
