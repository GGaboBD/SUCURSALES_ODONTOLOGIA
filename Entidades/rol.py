class Rol:
    def __init__(self, ID_rol: str, nombre_rol: str, descripcion_rol: str):
        self.ID_rol = ID_rol
        self.nombre_rol = nombre_rol
        self.descripcion_rol = descripcion_rol
        #En el ID quiero verificar que las primeras 4 letras del id inicien con un identificador unico yyy que el limite de caracteres sea de 10 
        if not self.ID_rol or self.ID_rol.strip() == "":
            raise ValueError("El ID del rol no puede estar vacío.")
        if not self.ID_rol.startswith("ROL_"):
            raise ValueError("El ID del rol debe comenzar con 'ROL_'.")
        if len(self.ID_rol) > 10:
            raise ValueError("El ID del rol no puede exceder los 10 caracteres.")
        if not self.nombre_rol:
            raise ValueError("El nombre del rol no puede estar vacío.")
        if not self.descripcion_rol:
            raise ValueError("La descripción del rol no puede estar vacía.")
        
        self.ID_rol = ID_rol
        self.nombre_rol = nombre_rol.strip()
        self.descripcion_rol = descripcion_rol.strip()
