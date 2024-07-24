from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item
# Нужный тип исключения для get_item()
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_email@mail.ru"
    }
    return render(request, "index.html", context)


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
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, "errors.html", {"error": f"Item with id={item_id} not found."})
    else:
        colors = item.colors.all()
        context= {
            "item": item,
            "colors": colors
            }
        return render(request, "item_page.html", context)


def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)