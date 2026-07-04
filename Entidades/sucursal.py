class Sucursal:
    def __init__(self, ID_sucursal: str, nombre_sucursal: str, direccion_sucursal: str, telefono_sucursal: str):
        self.ID_sucursal = ID_sucursal
        self.nombre_sucursal = nombre_sucursal
        self.direccion_sucursal = direccion_sucursal
        self.telefono_sucursal = telefono_sucursal

        #En el ID quiero verificar que las primeras 4 letras del id inicien con un identificador unico yyy que el limite de caracteres sea de 10 
        if not self.ID_sucursal or self.ID_sucursal.strip() == "":
            raise ValueError("El ID de la sucursal no puede estar vacío.")
        if not self.ID_sucursal.startswith("SUC_"):
            raise ValueError("El ID de la sucursal debe comenzar con 'SUC_'.")
        if len(self.ID_sucursal) > 10:
            raise ValueError("El ID de la sucursal no puede exceder los 10 caracteres.")

        if not self.nombre_sucursal or not self.nombre_sucursal.strip():
            raise ValueError("El nombre de la sucursal no puede estar vacío.")
        
        if not self.direccion_sucursal or not self.direccion_sucursal.strip():
            raise ValueError("La dirección de la sucursal no puede estar vacía.")
        
        if not self.telefono_sucursal or not self.telefono_sucursal.strip():
            raise ValueError("El teléfono de la sucursal no puede estar vacío.")

        self.ID_sucursal = ID_sucursal
        self.nombre_sucursal = nombre_sucursal.strip()
        self.direccion_sucursal = direccion_sucursal.strip()
        self.telefono_sucursal = telefono_sucursal.strip()
            
        