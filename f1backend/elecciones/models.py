from django.db import models

# Create your models here.
class Candidato:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.votos = 0

class Elecciones:
    def __init__(self) -> None:
        test = Candidato('Pepito', 'Skywalker')
        self.lista_candidatos = []

    def listar_candidatos(self):
        return self.lista_candidatos

    def buscar_candidato(self, nombre, apellido):
        for c in self.lista_candidatos:
            if c.nombre == nombre and c.apellido == apellido:
                return c
        return None
    
    # ----------------------------------------------------------------- #
    
    # 1
    def inscribir(self, candidato_obj):
        resultado = self.buscar_candidato(candidato_obj.nombre, candidato_obj.apellido)

        if resultado is None:
            self.lista_candidatos.append(candidato_obj)
            return 'Candidato registrado'
        return '(ERROR) El candidato ya existe...'

    # 2
    def votar(self, nombre, apellido):
        resultado = self.buscar_candidato(nombre, apellido)

        if isinstance(resultado, Candidato):
            resultado.votos += 1
            return f'Se ha votado por el candidato: {resultado.nombre} {resultado.apellido}'
        return 'Candidato no encontrado'
    
    # 3
    def resultado(self):
        votos = 0
        ganador = None
        for c in self.lista_candidatos:
            if c.votos > votos:
                ganador = c
                votos = c.votos
        return ganador
    
    # ----------------------------------------------------------------- #

    def actualizar(self, new_candidato):
        for c in self.lista_candidatos:
            c.nombre = new_candidato.nombre
            c.apellido = new_candidato.apellido
            return 'Candidato actualizado'
        return 'Candidato no registrado'
    
    def eliminar(self, nombre, apellido):
        resultado = self.buscar_candidato(nombre, apellido)

        if isinstance(resultado, Candidato):
            self.lista_candidatos.remove(resultado)
            return 'Candidato eliminado'
        return 'Candidato no encontrado'