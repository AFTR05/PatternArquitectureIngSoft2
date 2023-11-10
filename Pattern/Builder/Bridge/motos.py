# Implementaciones concretas de motos
from moto import MotoImplementacion

class MotoDeportivaImplementacion(MotoImplementacion):
    def conducir(self):
        return "Conduciendo una moto deportiva"

class MotoCalleImplementacion(MotoImplementacion):
    def conducir(self):
        return "Conduciendo una moto de calle"
