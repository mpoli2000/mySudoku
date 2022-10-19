from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from AppDoku.models import MiJuego
from AppDoku.forms import Form_Editar_MiJuego

from dokusan import solvers, generators, renderers
from dokusan.boards import BoxSize, Sudoku

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def misJuegos(request):
    return render(request, 'misJuegos.html')

@login_required
def opciones(request):
    return render(request, 'opciones.html')

def registro(request):
    # form = UserRegisterForm(request.POST)
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            #username = form.cleaned_data["username"]
            form.save()
            return redirect('/login')
        else:
            return render(request, "registro.html", {'form': form})
    else:
        form = UserCreationForm()
        # form = UserRegisterForm()
        return render(request, "registro.html", {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():           
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(username = user, password = pwd)
            if user is not None:
                login(request, user)
                return render(request, "misJuegos.html")
            else:
                return render(request, "login.html", {'form': form})
        else:
            return render(request, "login.html", {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == 'POST':
        # form = UserEditForm(request.POST, instance = usuario)
        form = UserChangeForm(request.POST, instance = usuario)
        if form.is_valid():
            #Datos a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return redirect('/perfil')
        else:
            return render(request, 'misJuegos.html', {'form': form})
    else:
        # form = UserEditForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        form = UserChangeForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        return render(request, 'editarPerfil.html', {'form': form, 'usuario': usuario})


@login_required
def cambiarClave(request):
    usuario = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = usuario)
        # form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            user =  form.save()
            update_session_auth_hash(request, user)
            return render(request, 'misJuegos.html')
        else:
            return render(request, 'misJuegos.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
        # form = ChangePasswordForm(user = request.POST) 
        return render(request, 'changepass.html', {'form': form, 'usuario': usuario})


@login_required
def verPerfil(request):
    return render(request, 'perfil.html')

#-----------------------------------------

@login_required
def listar_juegos(request):
    juegos = MiJuego.objects.all()
    return render(request, 'juegos/listar_juegos.html', {'juegos': juegos})

import datetime
@login_required
def crear_juegos(request):
    if request.method == 'POST':
        n = request.POST['nivel']
        sudoku = generators.random_sudoku(avg_rank=150)
        print(type(sudoku), sudoku, len(str(sudoku)))
        print(renderers.colorful(sudoku))
        juego = MiJuego(fecha = datetime.date(2022, 10, 19),
                        nombre = request.POST['nombre'],
                        descripcion = request.POST['descripcion'],
                        nivel = request.POST['nivel'],
                        sudoku_inicial = str(sudoku),
                        sudoku_final = str(sudoku),
                        numeros = 10,
                        ceros = 71,
                        progreso = 0,
                        movimientos = 0,
                        )
        juego.save()
        return redirect('/listar_juegos')
    return render(request, 'juegos/crear_juegos.html')

@login_required
def borrar_juegos(request, id_juego):
    juego = MiJuego.objects.get(id = id_juego)
    juego.delete()
    return redirect('/listar_juegos')

@login_required
def actualizar_juegos(request, id_juego):
    juego = MiJuego.objects.get(id = id_juego)
    if request.method == 'POST':
        formulario = Form_Editar_MiJuego(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            juego.nombre = info['nombre']
            juego.descripcion = info['descripcion']
            juego.save()

            return redirect('/listar_juegos')
    else:
        formulario = Form_Editar_MiJuego(initial={'nombre': juego.nombre,
                                           'descripcion': juego.descripcion,
                                           })
        return render(request, 'juegos/actualizar_juegos.html', {'formulario': formulario})

@login_required
def tablero(request, id_juego):
    juego = MiJuego.objects.get(id = id_juego)
    sudoku = Sudoku.from_string(juego.sudoku_final, box_size=BoxSize(3,3))
    print(renderers.colorful(sudoku))
    return render(request, 'juegos/tablero.html', {'juego': juego})