# Clases de manejadores concretos
from pedido import Pedido

class ManejadorPedido:
    def __init__(self):
        self.siguiente = None

    def manejar_pedido(self, pedido):
        if self.siguiente:
            return self.siguiente.manejar_pedido(pedido)
        return f"El pedido {pedido.nombre} ha sido rechazado"

class ManejadorVerificacionStock(ManejadorPedido):
    def manejar_pedido(self, pedido):
        if pedido.total <= 100:
            pedido.aprobar()
            return f"El pedido {pedido.nombre} ha sido aprobado por Verificación de Stock"
        return super().manejar_pedido(pedido)

class ManejadorVerificacionCredito(ManejadorPedido):
    def manejar_pedido(self, pedido):
        if pedido.total <= 500:
            pedido.aprobar()
            return f"El pedido {pedido.nombre} ha sido aprobado por Verificación de Crédito"
        return super().manejar_pedido(pedido)

class ManejadorAprobacionFinal(ManejadorPedido):
    def manejar_pedido(self, pedido):
        if pedido.aprobado:
            return f"El pedido {pedido.nombre} ha sido aprobado y procesado"
        return f"El pedido {pedido.nombre} ha sido rechazado"
