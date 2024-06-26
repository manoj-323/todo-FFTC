from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import HttpResponse

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('add-todo/', views.add_todo, name='signup'),
    path('logout/', views.signout, name='signout'),
    path('delete-todo/<int:id>', views.delete_todo, name='signout'),
    path('change-status/<int:id>/<str:status>', views.change_todo, name='signout'),
]