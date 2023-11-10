# Archivo principal para probar
from pedido import Pedido
from manejadores import (
    ManejadorVerificacionStock,
    ManejadorVerificacionCredito,
    ManejadorAprobacionFinal,
)

if __name__ == "__main__":
    pedido1 = Pedido("Pedido 1", 80)
    pedido2 = Pedido("Pedido 2", 450)
    pedido3 = Pedido("Pedido 3", 600)

    manejador_stock = ManejadorVerificacionStock()
    manejador_credito = ManejadorVerificacionCredito()
    manejador_aprobacion_final = ManejadorAprobacionFinal()

    # Configurar la cadena de responsabilidad
    manejador_stock.siguiente = manejador_credito
    manejador_credito.siguiente = manejador_aprobacion_final

    # Procesar pedidos
    resultado1 = manejador_stock.manejar_pedido(pedido1)
    resultado2 = manejador_stock.manejar_pedido(pedido2)
    resultado3 = manejador_stock.manejar_pedido(pedido3)

    print(resultado1)  # Salida: "El pedido Pedido 1 ha sido aprobado por Verificación de Stock"
    print(resultado2)  # Salida: "El pedido Pedido 2 ha sido aprobado por Verificación de Crédito"
    print(resultado3)  # Salida: "El pedido Pedido 3 ha sido rechazado"
