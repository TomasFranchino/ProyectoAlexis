from django.urls import path
from . import views
from django.conf.urls import handler404


 
handler404 = views.handler404

urlpatterns = [
    path('home', views.Login,name='index'),
    path('logouts', views.Logout,name='logouts'),
    path('',views.Home,name='home'),
    path('publicacion/<int:pk>/', views.Publicacion_detalle, name='publicacion_detalle'),
    path('fav/<int:pk>/', views.Fav, name='fav'),
    path('publicacion/nueva', views.Publicacion_nueva, name='publicacion_nueva'),
    path('publicacion/<int:pk>/editar/', views.Publicacion_editar, name='publicacion_editar'),
    path('publicacion/<int:pk>/eliminar/', views.Publicacion_eliminar, name='publicacion_eliminar'),
    path('tendencias', views.Tendencias, name='tendencias'),
    path('estilo', views.Estilo, name='estilo'),
    path('register', views.Register, name='register'),
    path('cambiar_contraseña', views.Recuperar_contraseña, name='cambiar_contraseña'), 
] 