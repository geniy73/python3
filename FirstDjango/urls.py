from MainApp import views

from django.urls import path

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('item', views.item),

]
