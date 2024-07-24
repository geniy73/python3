from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# author = {
#     "Имя" : "Иван",
#     "Отчество" : "Петрович",
#     "Фамилия" : "Иванов",
#     "Телефон" : "8-923-600-01-02",
#     "email" : "ivan@mail.ru",
# }



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
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, "errors.html", {"error": f"Item with id={item_id} not found."})
    else:
        context= {"item": item}
        return render(request, "item_page.html", context)

def items_list(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, 'items_list.html', context)