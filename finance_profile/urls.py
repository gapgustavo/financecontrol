from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('manage/', views.manage, name="manage"),
    path('add_wallet/', views.add_wallet, name="add_wallet"),
    path('delete_wallet/<int:id>', views.delete_wallet, name="delete_wallet"),
    path('add_categorie/', views.add_categorie, name="add_categorie"),
]
