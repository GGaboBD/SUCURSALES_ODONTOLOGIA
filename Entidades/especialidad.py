class Especialidad:
    def __init__(self, ID_especialidad: str, nombre_especialidad: str, descripcion_especialidad: str):
        self.ID_especialidad = ID_especialidad
        self.nombre_especialidad = nombre_especialidad
        self.descripcion_especialidad = descripcion_especialidad
        #En el ID quiero verificar que las primeras 4 letras del id inicien con un identificador unico yyy que el limite de caracteres sea de 10 
        if not self.ID_especialidad or self.ID_especialidad.strip() == "":
            raise ValueError("El ID de la especialidad no puede estar vacío.")
        if not self.ID_especialidad.startswith("ESP_"):
            raise ValueError("El ID de la especialidad debe comenzar con 'ESP_'.")
        if len(self.ID_especialidad) > 10:
            raise ValueError("El ID de la especialidad no puede exceder los 10 caracteres.")
        if not self.nombre_especialidad:
            raise ValueError("El nombre de la especialidad no puede estar vacío.")
        if not self.descripcion_especialidad:
            raise ValueError("La descripción de la especialidad no puede estar vacía.")
        
        self.ID_especialidad = ID_especialidad
        self.nombre_especialidad = nombre_especialidad.strip()
        self.descripcion_especialidad = descripcion_especialidad.strip()
