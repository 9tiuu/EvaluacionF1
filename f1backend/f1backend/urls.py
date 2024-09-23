from django.contrib import admin
from django.urls import path

from elecciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('formulario/', views.formulario, name="form"),
    path('votar/', views.votar, name="votar"),
    path('inscripcion/', views.inscripcion, name='inscripcion'),
    path('registro/', views.registro, name='registro'),
    path('resultados/', views.resultados, name='resultados'),

    path('actualizar/<str:nombre>/<str:apellido>/', views.actualizar, name='actualizar'),
    path('confirm_actualizar/', views.confirm_actualizar, name='confirm_actualizar'),

    path('eliminar/<str:nombre>/<str:apellido>/', views.eliminar, name='eliminar'),
    path('confirm_eliminar/', views.confirm_eliminar, name='confirm_eliminar'),
]
