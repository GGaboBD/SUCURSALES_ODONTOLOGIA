from Entidades.sucursal import Sucursal
#Todo esto se conectara a una base de datos por medio de una API

class Paciente:
    def __init__(self, ID_paciente: str, nombre_paciente: str, DUI_paciente: str, telefono_paciente: str, sucursal: Sucursal):
        self.ID_paciente = ID_paciente
        self.nombre_paciente = nombre_paciente
        self.DUI_paciente = DUI_paciente
        self.telefono_paciente = telefono_paciente
        self.sucursal = sucursal
        #En el ID quiero verificar que las primeras 4 letras del id inicien con un identificador unico yyy que el limite de caracteres sea de 10 
        if not self.ID_paciente or self.ID_paciente.strip() == "":
            raise ValueError("El ID del paciente no puede estar vacío.")
        if not self.ID_paciente.startswith("PAC_"):
            raise ValueError("El ID del paciente debe comenzar con 'PAC_'.")
        if len(self.ID_paciente) > 10:
            raise ValueError("El ID del paciente no puede exceder los 10 caracteres.")
        if not self.nombre_paciente:
            raise ValueError("El nombre del paciente no puede estar vacío.")
        if not self.DUI_paciente:
            raise ValueError("El DUI del paciente no puede estar vacío.")
        if not self.telefono_paciente:
            raise ValueError("El teléfono del paciente no puede estar vacío.")
        if not self.sucursal:
            raise ValueError("La sucursal del paciente no puede estar vacía.")

