from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
author = {
    "Имя" : "Иван",
    "Отчество" : "Петрович",
    "Фамилия" : "Иванов",
    "Телефон" : "8-923-600-01-02",
    "email" : "ivan@mail.ru",
}

items = [
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
    return render(request, 'index.html')

def about(request):
    
    text=f"""
    <p>Имя: <strong>{author["Имя"]}</strong></p>
    <p>Отчество: <strong>{author["Отчество"]}</strong></p>
    <p>Фамилия: <strong>{author["Фамилия"]}</strong></p>
    <p>Телефон: <strong>{author["Телефон"]}</strong></p>
    <p>Эл.почта: <strong>{author["email"]}</strong></p>
    """
    return HttpResponse(text)

def get_item(request, item_id):
    """ По указанному id возвращаем имя и кол-во элемента """
    for item in items:
        if item['id'] == item_id:
            result = f"""
            <h2> Имя: {item["name"]} </h2>
            <p> Количество: {item["quantity"]} </p>
            <p><a href="/items">Назад к списку товаров </a></p>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f"Item with id={item_id} not found.")

def get_items(request):
    result = "<h1>Список товаров<h1><ol>"
    for item in items:
        result += f"""<li> <a href="/item/{item['id']}"> {item['name']}</li>"""
    result += "</ol>"
    return HttpResponse(result)