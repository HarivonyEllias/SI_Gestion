from django.urls import path

from . import views

urlpatterns = [
    path('choose', views.Choose, name='choose'),
    path('index', views.index, name='index'),
    path('form', views.Create_form , name='form'),
    path('list', views.list_company , name='list'),
    path('get_id_name/<int:idsociete>/<str:nom>', views.get_id_name, name='get_id_name'),    
    path('log', views.log , name='log'),
    path('insert_count', views.insert_count , name='insert_count'),
    path('add', views.insert_company, name='add'),
]
