import re
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

menu = [
    {"title": "О сайте", "url_name": "lime:about"},
    {"title": "Добавить товар", "url_name": "lime:add_item"},
    {"title": "Обратная связь", "url_name": "lime:contact"},
    {"title": "Войти", "url_name": "lime:login"},
]

data_db = [
    {
        "id": 1,
        "title": "Букет роз",
        "content": "Биография роз",
        "is_published": True,
    },
    {
        "id": 2,
        "title": "Букет Невеста",
        "content": "Свадебный букет",
        "is_published": False,
    },
    {
        "id": 3,
        "title": "Букет + рафаэлло",
        "content": "Приятное и полезное",
        "is_published": True,
    },
]


def index(request):
    data = {
        "title": "Главная страница",
        "menu": menu,
        "item": data_db,
    }
    return render(request, "lime/index.html", context=data)


def about(request):
    data = {
        "title": "О нас",
        "menu": menu,
    }
    return render(request, "lime/about.html", context=data)




def additem(request):
    return HttpResponse("Добавление товара")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

def show_item(request, item_id):
    data = {
        "title": "подробно о товаре",
        "item_id": item_id,
    }
    return render(request, 'lime/show_item.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
