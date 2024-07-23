from MainApp import views

from django.urls import path

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('item/<int:id>', views.item),
    path('items', views.items),

]
