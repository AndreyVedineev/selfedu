from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Главная страница приложения Lime")


def about(request):
    return HttpResponse("Страница о нас приложения  Lime")

def categories(request, cat_id):
    return HttpResponse(f'<h1>Категория товара</h1><p>id: {cat_id}</p>')

def archive(request, year):
    return HttpResponse(f'<h1>Архив</h1><p>ГОД: {year}</p>')
