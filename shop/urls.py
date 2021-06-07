from django.urls import path
from . import views
urlpatterns = [
    path('',views.firstFun,name='firstFun'),
    path('login',views.login,name='login'),
    path('getCategories',views.getCategories,name='getCategories'),
    path('getItemsForCategory/<int:categoryId>',views.getItemsForCategory,name='getItemsForCategory'),
]