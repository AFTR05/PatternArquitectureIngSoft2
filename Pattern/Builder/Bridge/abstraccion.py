# Clase base para la abstracción de motos
from moto import MotoImplementacion

class MotoAbstraccion:
    def __init__(self, implementacion):
        self._implementacion = implementacion

    def conducir(self):
        pass
