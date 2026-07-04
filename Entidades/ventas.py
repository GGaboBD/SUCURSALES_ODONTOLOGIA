from Entidades.sucursal import Sucursal
#Todo esto se conectara a una base de datos por medio de una API
class Ventas:
    def __init__(self, ID_ventas: str, fecha_ventas: str, monto_venta: float, sucursal: Sucursal):
        self.ID_ventas = ID_ventas
        self.fecha_ventas = fecha_ventas
        self.monto_venta = monto_venta
        self.sucursal = sucursal

        #En el ID quiero verificar que las primeras 4 letras del id inicien con un identificador unico yyy que el limite de caracteres sea de 10 
        if not self.ID_ventas or self.ID_ventas.strip() == "":
            raise ValueError("El ID de la venta no puede estar vacío.")
        if not self.ID_ventas.startswith("VEN_"):
            raise ValueError("El ID de la venta debe comenzar con 'VEN_'.")
        if len(self.ID_ventas) > 10:
            raise ValueError("El ID de la venta no puede exceder los 10 caracteres.")
        if not self.fecha_ventas:
            raise ValueError("La fecha de la venta no puede estar vacía.")
        if self.monto_venta < 0:
            raise ValueError("El monto de la venta no puede ser un número negativo.")
        if not self.sucursal:
            raise ValueError("La sucursal de la venta no puede estar vacía.")