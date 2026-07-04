from Entidades.especialidad import Especialidad, especialidad
from Entidades.sucursal import Sucursal

class Doctor:
    def __init__(self, ID_doctor: str, nombre_doctor: str, especialidad: Especialidad, sucursal: Sucursal, doctor_JVPO: str):
        self.ID_doctor = ID_doctor
        self.nombre_doctor = nombre_doctor
        self.especialidad = especialidad
        self.sucursal = sucursal
        self.doctor_JVPO = doctor_JVPO
        self.Disponibilidad = "activo"
        #En el ID quiero verificar que las primeras 4 letras del id inicien con un identificador unico yyy que el limite de caracteres sea de 10 
        if not self.ID_doctor or self.ID_doctor.strip() == "":
            raise ValueError("El ID del doctor no puede estar vacío.")
        if not self.ID_doctor.startswith("DOC_"):
            raise ValueError("El ID del doctor debe comenzar con 'DOC_'.")
        if len(self.ID_doctor) > 10:
            raise ValueError("El ID del doctor no puede exceder los 10 caracteres.")
        if not self.nombre_doctor:
            raise ValueError("El nombre del doctor no puede estar vacío.")
        if not self.especialidad:
            raise ValueError("La especialidad del doctor no puede estar vacía.")
        if not self.sucursal:
            raise ValueError("La sucursal del doctor no puede estar vacía.")
        if not self.doctor_JVPO:
            raise ValueError("El doctor debe tener un número de la Junta de Vigilancia de Profesionales Odontológicos (JVPO) válido.")



    def cambiar_disponibilidad(self, nueva_disponibilidad: str):
        if nueva_disponibilidad not in ["activo", "inactivo"]:
            raise ValueError("La disponibilidad debe ser 'activo' o 'inactivo'.")
        self.Disponibilidad = nueva_disponibilidad
    
    