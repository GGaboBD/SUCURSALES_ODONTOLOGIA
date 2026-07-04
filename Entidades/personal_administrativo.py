from Entidades.rol import Rol
from Entidades.sucursal import Sucursal

class personal_administrativo:
    def __init__(self, ID_personal_admin: str, nombre_personal_admin: str, rol: Rol, sucursal: Sucursal):
        self.ID_personal_admin = ID_personal_admin
        self.nombre_personal_admin = nombre_personal_admin
        self.rol = rol
        self.sucursal = sucursal
        self.Disponibilidad = "activo"
        #En el ID quiero verificar que las primeras 4 letras del id inicien con un identificador unico yyy que el limite de caracteres sea de 10 
        if not self.ID_personal_admin or self.ID_personal_admin.strip() == "":
            raise ValueError("El ID del personal administrativo no puede estar vacío.")
        if not self.ID_personal_admin.startswith("ADM_"):
            raise ValueError("El ID del personal administrativo debe comenzar con 'ADM_'.")
        if len(self.ID_personal_admin) > 10:
            raise ValueError("El ID del personal administrativo no puede exceder los 10 caracteres.")
        if not self.nombre_personal_admin:
            raise ValueError("El nombre del personal administrativo no puede estar vacío.")
        if not self.rol:
            raise ValueError("El rol del personal administrativo no puede estar vacío.")
        if not self.sucursal:
            raise ValueError("La sucursal del personal administrativo no puede estar vacía.")
        


    def cambiar_disponibilidad(self, nueva_disponibilidad: str):
        if nueva_disponibilidad not in ["activo", "inactivo"]:
            raise ValueError("La disponibilidad debe ser 'activo' o 'inactivo'.")
        self.Disponibilidad = nueva_disponibilidad
    
    