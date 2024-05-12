from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("Главная страница приложения Lime")


def about(request):
    return HttpResponse("Страница о нас приложения  Lime")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Категория товара</h1><p>id: {cat_id}</p>")


def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f"<h1>Архив</h1><p>ГОД: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
