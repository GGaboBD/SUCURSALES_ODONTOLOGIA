from Entidades.sucursal import Sucursal

class Paciente:
    def __init__(self, ID_paciente: int, nombre_paciente: str, DUI_paciente: str, telefono_paciente: str, sucursal: Sucursal):
        self.ID_paciente = ID_paciente
        self.nombre_paciente = nombre_paciente
        self.DUI_paciente = DUI_paciente
        self.telefono_paciente = telefono_paciente
        self.sucursal = sucursal

