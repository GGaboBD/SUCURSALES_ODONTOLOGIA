from Entidades.rol import Rol
from Entidades.sucursal import Sucursal

class personal_administrativo:
    def __init__(self, nombre_personal_admin: str, rol: Rol, sucursal: Sucursal):
        self.nombre_personal_admin = nombre_personal_admin
        self.rol = rol
        self.sucursal = sucursal