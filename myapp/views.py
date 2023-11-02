from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login, get_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Publicacion
from django.utils import timezone
from .forms import PublicacionForm
from .trends import TituloTendencias, ContenidoTendencias, UrlTendencias
from .recuperar_contraseña import Recuperacion, GenerarCodigo
from django.contrib.auth.password_validation import validate_password

# Create your views here.


def Login(request):
    error_message = None

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error_message = "Credenciales incorrectas."

    return render(request, "registration/login.html", {"error_message": error_message})


def Logout(request):
    logout(request)
    return redirect("/")


def Home(request, estilo=False):
    publicaciones = Publicacion.objects.filter(respuesta_a=None).order_by(
        "fecha_publicacion"
    )
    respuestas = Publicacion.objects.exclude(respuesta_a=None).order_by(
        "fecha_publicacion"
    )
    usuario = get_user(request)
    print(usuario.username)
    # form = PublicacionForm(request.POST)
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
            else:
                return redirect("index")
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect("home")
    else:
        form = PublicacionForm()
        form.fields
    if estilo == True:
        estilo = "publicaciones2.css"
    else:
        estilo = "publicaciones.css"
    return render(
        request,
        "index.html",
        {
            "publicaciones": publicaciones,
            "usuario": usuario,
            "respuestas": respuestas,
            "form": form,
            "estilo": estilo,
        },
    )


def Publicacion_detalle(request, pk):
    publicaciones = get_object_or_404(Publicacion, pk=pk)
    respuestas = Publicacion.objects.filter(respuesta_a=publicaciones).order_by(
        "fecha_publicacion"
    )
    usuario = get_user(request)

    return render(
        request,
        "publicaciones_detalle.html",
        {"publicaciones": publicaciones, "usuario": usuario, "respuestas": respuestas},
    )


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
            return redirect("home")
    else:
        form = PublicacionForm()
        form.fields
    return render(
        request, "publicaciones_editar.html", {"form": form, "usuario": usuario}
    )


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
            return redirect("publicacion_detalle", pk=post.pk)
    else:
        form = PublicacionForm(instance=post)
    return render(
        request, "publicaciones_editar.html", {"form": form, "usuario": usuario}
    )


@login_required
def Publicacion_eliminar(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    context = {}
    if request.method == "GET":
        # delete object
        post.delete()
        return redirect("home")
    return render(request, "publicacion_detalle.html", {"publicacion": post})


def Tendencias(request):
    titulos = TituloTendencias()
    contenidos = ContenidoTendencias()
    url = UrlTendencias()
    usuario = get_user(request)
    datos = zip(titulos, contenidos, url)
    return render(request, "tendencias.html", {"datos": datos, "usuario": usuario})


def Fav(request, pk):
    publicacion = Publicacion.objects.get(pk=pk)
    if publicacion.fav == 1:
        publicacion.quitar_fav()
    else:
        publicacion.agregar_fav()

    return redirect("home")


def Estilo(request):
    estilo = True
    return Home(request, estilo)


def Register(request):
    error_message = None
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = request.POST["email"]
            user.save()
            return redirect("index")
        else:
            error_message = "Credenciales incorrectas."

    else:
        form = UserCreationForm()
        form.fields
    return render(
        request, "register.html", {"form": form, "error_message": error_message}
    )


def Recuperar_contraseña(request):
    error_message = None

    if request.method == "GET":
        codigo = GenerarCodigo(1)
        if "username" in request.GET:
            user = get_object_or_404(User, username=request.GET["username"])
            Recuperacion(user.email, codigo)
    elif request.method == "POST":
        codigo_ingresado = request.POST.get("codigo")
        username = request.GET.get("username")
        if not codigo_ingresado or not username:
            error_message = "Falta el código o la contraseña."
        else:
            user = get_object_or_404(User, username=username)
            codigo = GenerarCodigo(2)
            if codigo == codigo_ingresado:
                contra = request.POST.get("password")
                if not contra:
                    error_message = "Falta la contraseña."
                else:
                    if validate_password(contra, user=user) == None:
                        user.set_password(contra)
                        user.save()
                        return redirect("index")
                    else:
                        error_message = "La contraseña no es valida"
            else:
                error_message = "El código es incorrecto"

    return render(request, "cambio_contraseña.html", {"error_message": error_message})


def handler404(request, exception=None):
    return render(request, "404.html", status=404)


# Error 404, statics,
