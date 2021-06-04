from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def firstFun(request):
    return HttpResponse("You Either Die a hero, or you live long enough to see yourself become a villian")