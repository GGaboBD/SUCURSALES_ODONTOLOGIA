from Entidades.sucursal import Sucursal

class Ventas:
    def __init__(self, ID_ventas: int, fecha_ventas: str, monto_venta: float, sucursal: Sucursal):
        self.ID_ventas = ID_ventas
        self.fecha_ventas = fecha_ventas
        self.monto_venta = monto_venta
        self.sucursal = sucursal