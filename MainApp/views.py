from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def home(request):
    text="""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Губарев А.В.</i>
    """
    return HttpResponse(text)

def about(request):
    firstname = "Иван"
    surname = "Петрович"
    lastname = "Иванов"
    phonenumber = "8-923-600-01-02"
    email = "ivan@mail.ru"
    
    text="""f"<p>Имя:<strong>{firstname}</strong></p>
                <p>Отчество:<strong>{surname}</strong></p>
                <p>Фамилия:<strong>{lastname}</strong></p>
                <p>Телефон:<strong>{phonenumber}</strong></p>
                <p>Эл.почта:<strong>{email}</strong></p>"
        """
    return HttpResponse(text)