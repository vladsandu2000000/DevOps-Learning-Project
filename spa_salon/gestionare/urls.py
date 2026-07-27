from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pacienti/', views.lista_pacienti, name='lista_pacienti'),
    path('pacienti/adauga/', views.adauga_pacient, name='adauga_pacient'),
    path('pacienti/editeaza/<int:id>/', views.editeaza_pacient, name='editeaza_pacient'),
    path('pacienti/sterge/<int:id>/', views.sterge_pacient, name='sterge_pacient'),
    path('tratamente/', views.lista_tratamente, name='lista_tratamente'),
    path('tratamente/adauga/', views.adauga_tratament, name='adauga_tratament'),
    path('tratamente/editeaza/<int:id>/', views.editeaza_tratament, name='editeaza_tratament'),
    path('tratamente/sterge/<int:id>/', views.sterge_tratament, name='sterge_tratament'),
    path('diagnoze/', views.lista_diagnoze, name='lista_diagnoze'),
]
