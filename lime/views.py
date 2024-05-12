from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'lime/index.html')


def about(request):
    return render(request, 'lime/about.html')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Категория товара</h1><p>id: {cat_id}</p>")


def archive(request, year):
    if year > 2023:
        return redirect('index')
    return HttpResponse(f"<h1>Архив</h1><p>ГОД: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
