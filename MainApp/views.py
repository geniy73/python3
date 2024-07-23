from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
author = {
    "Имя" : "Иван",
    "Отчество" : "Петрович",
    "Фамилия" : "Иванов",
    "Телефон" : "8-923-600-01-02",
    "email" : "ivan@mail.ru",
}

# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 7, "name": "Картофель фри" ,"quantity":0},
#    {"id": 8, "name": "Кепка" ,"quantity":124},
# ]

def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_email@mail.com"
    }
    return render(request, 'index.html', context)

def about(request):
    author = {
        "name": "Иван",
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
    return render(request, "about.html", {"author": author})

def get_item(request, item_id):
    """ По указанному id возвращаем имя и кол-во элемента """
    if Item.objects.get(id=item_id).id == item_id:
        context = {
                "item": Item.objects.get(id=item_id)
                    }  
        return render(request, 'item_page.html', context)

def get_items(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, 'items_list.html', context)