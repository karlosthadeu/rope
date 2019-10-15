from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import UsuarioView

urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(),     name='entrar'),
    path('sair/',   auth_views.LogoutView.as_view(),    name='sair'),

    path('criar/',        UsuarioView.criar,      name='conta_criar'),
]
