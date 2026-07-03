class Sucursal:
    def __init__(self, ID_sucursal: int, nombre_sucursal: str, direccion_sucursal: str, telefono_sucursal: str):
        self.ID_sucursal = ID_sucursal
        self.nombre_sucursal = nombre_sucursal
        self.direccion_sucursal = direccion_sucursal
        self.telefono_sucursal = telefono_sucursal

        if self.ID_sucursal <= 0:
            raise ValueError("El ID de la sucursal debe ser un número positivo")
        
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
            
        