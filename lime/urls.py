from atexit import register
from django.urls import path, register_converter

from lime import views
from . import converters

app_name = "lime"
register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("cats/<int:cat_id>", views.categories, name="cats"),
    path("archive/<year4:year>", views.archive, name="archive"),
]
