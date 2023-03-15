from django.urls import path

from . import views

urlpatterns = [
    path('choose', views.Choose, name='choose'),
    path('index', views.index, name='index'),
    path('form', views.Create_form , name='form'),
    path('add', views.insert_company, name='add'),
]
