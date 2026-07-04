from Entidades.sucursal import Sucursal
#Todo esto se conectara a una base de datos por medio de una API
class Ventas:
    def __init__(self, ID_ventas: int, fecha_ventas: str, monto_venta: float, sucursal: Sucursal):
        self.ID_ventas = ID_ventas
        self.fecha_ventas = fecha_ventas
        self.monto_venta = monto_venta
        self.sucursal = sucursal

        if self.ID_ventas <= 0:
            raise ValueError("El ID de la venta debe ser un número positivo.")
        if not self.fecha_ventas:
            raise ValueError("La fecha de la venta no puede estar vacía.")
        if self.monto_venta < 0:
            raise ValueError("El monto de la venta no puede ser un número negativo.")
        if not self.sucursal:
            raise ValueError("La sucursal de la venta no puede estar vacía.")