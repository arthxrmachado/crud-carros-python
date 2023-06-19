from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, alterar, atualizar, deletar

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvar"),
    path('alterar/<int:id>', alterar, name='alterar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
    path('deletar/<int:id>', deletar, name='deletar'),
]
