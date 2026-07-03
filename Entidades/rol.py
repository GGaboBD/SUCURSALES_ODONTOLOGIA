class Rol:
    def __init__(self, ID_rol: int, nombre_rol: str, descripcion_rol: str):
        self.ID_rol = ID_rol
        self.nombre_rol = nombre_rol
        self.descripcion_rol = descripcion_rol

        if self.ID_rol <= 0:
            raise ValueError("El ID del rol debe ser un número positivo.")
        if not self.nombre_rol:
            raise ValueError("El nombre del rol no puede estar vacío.")
        if not self.descripcion_rol:
            raise ValueError("La descripción del rol no puede estar vacía.")
        
        self.ID_rol = ID_rol
        self.nombre_rol = nombre_rol.strip()
        self.descripcion_rol = descripcion_rol.strip()
