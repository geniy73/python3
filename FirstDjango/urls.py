from MainApp import views

from django.urls import path

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('item/<int:item_id>', views.get_item, name="item-detail"),
    path('items', views.items_list, name="items-list"),

]
