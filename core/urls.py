from django.urls import path
from .views import *

urlpatterns = [
    path("",root,name="root"),

    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("register", register_view, name="register"),

    path("painel", painel, name="painel"),

    path("crud", crud_view, name="crud"),
    path("crud/create", crud_create),
    path("crud/delete/<int:id_aviso>", crud_delete),
    path("crud/update/<int:id_aviso>", crud_update),
    
]