from django.shortcuts import render
from .models import Elecciones, Candidato

e = Elecciones()

# Create your views here.
def home(request):
    return render(request, 'elecciones/home.html')

def formulario(request):
    return render(request, 'elecciones/formulario.html')

# ----------------------------------------------------------------- #

# 1
def votar(request):
    return render(request, 'elecciones/votar.html', {'candidatos':e.listar_candidatos()})

# 2
def inscripcion(request):
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')

    if nombre != '' or apellido != '':
        candidato = Candidato(nombre, apellido)
        mensaje = e.inscribir(candidato)
    else:
        mensaje = 'Campos vacios'

    return render(request, 'elecciones/inscripcion.html', {'mensaje':mensaje})

# 3
def registro(request):
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')

    if nombre != '' or apellido != '':
        mensaje = e.votar(nombre, apellido)
    else:
        mensaje = 'Campos vacios'

    return render(request, 'elecciones/registro.html', {'mensaje':mensaje})

# 4
def resultados(request):
    return render(request, 'elecciones/resultados.html', {'ganador':e.resultado()})

# ----------------------------------------------------------------- #

def actualizar(request, nombre, apellido):
    candidato = e.buscar_candidato(nombre, apellido)

    if candidato is not None:
        return render(request, 'elecciones/actualizar.html', {'candidato':candidato})
    else:
        return render(request, 'elecciones/actualizar.html', {'mensaje':'Candidato no encontrado...'})
    
def confirm_actualizar(request):
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')

    asd = e.buscar_candidato(nombre, apellido)

    if nombre.strip() == '' or apellido.strip() == '':
        mensaje = 'Campos vacios'
    else:
        candidato = Candidato(nombre, apellido)
        mensaje = e.actualizar(candidato)

    return render(request, 'elecciones/c_actualizar.html', {'mensaje':mensaje})

# ----------------------------------------------------------------- #

def eliminar(request, nombre, apellido):
    candidato = e.buscar_candidato(nombre, apellido)

    if candidato is not None:
        return render(request, 'elecciones/eliminar.html', {'candidato':candidato})
    
def confirm_eliminar(request):
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')

    if nombre.strip() == '' or apellido.strip() == '':
        mensaje = 'Campos vacios'
    else:
        mensaje = e.eliminar(nombre, apellido)

    return render(request, 'elecciones/c_actualizar.html', {'mensaje':mensaje})