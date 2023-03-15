from django.urls import path

from . import views

urlpatterns = [
    path('choose', views.Choose, name='choose'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('login_validation', views.login_validation, name='login_validation'),
    path('form', views.Create_form , name='form')
]
