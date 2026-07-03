from Entidades.rol import Rol
from Entidades.sucursal import Sucursal
#Todo esto se conectara a una base de datos por medio de una API

class personal_administrativo:
    def __init__(self, ID_personal_admin: int, nombre_personal_admin: str, rol: Rol, sucursal: Sucursal):
        self.ID_personal_admin = ID_personal_admin
        self.nombre_personal_admin = nombre_personal_admin
        self.rol = rol
        self.sucursal = sucursal
        self.Disponibilidad = "activo"

        if self.ID_personal_admin <= 0:
            raise ValueError("El ID del personal administrativo debe ser un número positivo.")
        if not self.nombre_personal_admin:
            raise ValueError("El nombre del personal administrativo no puede estar vacío.")
        if not self.rol:
            raise ValueError("El rol del personal administrativo no puede estar vacío.")
        if not self.sucursal:
            raise ValueError("La sucursal del personal administrativo no puede estar vacía.")
        

# quiero agregar un metodo que me permita cambiar la disponibilidad del personal administrativo, para que pueda ser activado o desactivado según sea necesario.

    def cambiar_disponibilidad(self, nueva_disponibilidad: str):
        if nueva_disponibilidad not in ["activo", "inactivo"]:
            raise ValueError("La disponibilidad debe ser 'activo' o 'inactivo'.")
        self.Disponibilidad = nueva_disponibilidad
    
    