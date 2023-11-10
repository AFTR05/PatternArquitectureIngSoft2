# Clase base para el pedido
class Pedido:
    def __init__(self, nombre, total):
        self.nombre = nombre
        self.total = total
        self.aprobado = False

    def aprobar(self):
        self.aprobado = True
