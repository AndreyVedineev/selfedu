from atexit import register
from django.urls import path, register_converter

from lime import views
from . import converters

app_name = "lime"
register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path('additem/', views.additem, name='add_item'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('item/<int:item_id>/', views.show_item, name='item'),
    
]
