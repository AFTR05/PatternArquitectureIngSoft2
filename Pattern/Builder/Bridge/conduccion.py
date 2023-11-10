# Abstracciones concretas de la conducción de motos
from abstraccion import MotoAbstraccion

class ConduccionDiurna(MotoAbstraccion):
    def conducir(self):
        return f"{self._implementacion.conducir()} durante el día"

class ConduccionNocturna(MotoAbstraccion):
    def conducir(self):
        return f"{self._implementacion.conducir()} durante la noche"
