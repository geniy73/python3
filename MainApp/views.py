from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
author = {
    "Имя" : "Иван",
    "Отчество" : "Петрович",
    "Фамилия" : "Иванов",
    "Телефон" : "8-923-600-01-02",
    "email" : "ivan@mail.ru",
}

goods = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    text="""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Губарев А.В.</i>
    """
    return HttpResponse(text)

def about(request):
    
    text=f"""
    <p>Имя: <strong>{author["Имя"]}</strong></p>
    <p>Отчество: <strong>{author["Отчество"]}</strong></p>
    <p>Фамилия: <strong>{author["Фамилия"]}</strong></p>
    <p>Телефон: <strong>{author["Телефон"]}</strong></p>
    <p>Эл.почта: <strong>{author["email"]}</strong></p>
    """
    return HttpResponse(text)

def item(request, id):
    ids = []
    for x in goods:
        idx = ids.append(x.get("id"))
        if x.get("id") == id:
            idx = x.get("id")
            name = x.get("name")
            quantity = x.get("quantity")
    
    if id == 10:
        text = f'<h1>Товар с id=10 не найден!</h1>'
    elif id not in ids:
        text = f'<h1>Введен неверный код товара!</h1>'
    else:
        text = f"""<h1>Карточка товара</h1>
             <p>Наименование: <strong>{name}</strong></p>
             <p>Количество: <strong>{quantity} шт.</strong></p>
             """
    return HttpResponse(text)

def items(request):

    for x in goods:
        idx = x.get("id")
        name = x.get("name")
        quantity = x.get("quantity")
        text=f"""<h1>Каталог</h1>
                <p>{idx} {name} {quantity}</p>
    """
    return HttpResponse(text)