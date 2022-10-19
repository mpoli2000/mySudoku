from django.urls import path
from AppDoku.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),    
    path('misJuegos/', misJuegos),
    path('opciones/', opciones),
    path('crear_juegos/', crear_juegos),
    path('listar_juegos/', listar_juegos),
    path('actualizar_juegos/<id_juego>', actualizar_juegos),
    path('borrar_juegos/<id_juego>', borrar_juegos),
    path('tablero/<id_juego>', tablero),
    path('registro/', registro),
    path('login/', login_request),
    path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name="Logout"),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/cambiarClave/', cambiarClave),
    path('perfil/', verPerfil),
]