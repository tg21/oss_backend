from django.urls import path
from . import views
urlpatterns = [
    path('',views.firstFun,name='firstFun'),
    path('login',views.login,name='login'),
]