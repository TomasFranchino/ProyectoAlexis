from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login, get_user
from .models import Publicacion
from django.utils import timezone
from .forms import PublicacionForm
from .trends import TituloTendencias, ContenidoTendencias, UrlTendencias

# Create your views here.

def Login(request):
    error_message = None
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Home(request, username)
        else:
            error_message = "Credenciales incorrectas."

    return render(request, 'registration/login.html', {'error_message': error_message})

def Logout(request):
    logout(request)
    return redirect('/')

def Home(request):
    publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    usuario = get_user(request)
    return render(request, 'index.html', {'publicaciones': publicaciones,'usuario':usuario})

def Publicacion_detalle(request, pk):
    publicaciones = get_object_or_404(Publicacion, pk=pk)
    usuario = get_user(request)
    return render(request, 'publicaciones_detalle.html', {'publicaciones': publicaciones,'usuario':usuario})
@login_required
def Publicacion_nueva(request):
    usuario = get_user(request)
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PublicacionForm()
    return render(request, 'publicaciones_editar.html', {'form': form,'usuario':usuario})
@login_required
def Publicacion_editar(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    usuario = get_user(request)
    if request.method == "POST":
        form = PublicacionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autot = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('publicacion_detalle', pk=post.pk)
    else:
        form = PublicacionForm(instance=post)
    return render(request, 'publicaciones_editar.html', {'form': form,'usuario':usuario})
@login_required
def Publicacion_eliminar(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    context={}
    if request.method =="GET":
        # delete object
        post.delete()
        return redirect("home")
    return render(request, 'publicacion_detalle.html', {'publicacion': post})

def Tendencias(request):
    titulos = TituloTendencias()
    contenidos = ContenidoTendencias()
    url = UrlTendencias()
    usuario = get_user(request)
    datos = zip(titulos, contenidos,url)
    return render(request, 'tendencias.html', {'datos': datos,'usuario':usuario})

def handler404(request,exception=None):
    return render(request,'404.html',status=404)

# Error 404, statics, 