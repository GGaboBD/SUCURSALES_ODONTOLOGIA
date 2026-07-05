from datetime import date
 
 
class Servicio:
    def __init__(self, id_servicio: str, descripcion_servicio: str, id_doctor: str):
        # El ID debe iniciar con "SERV_" y no exceder 10 caracteres
        if not id_servicio or id_servicio.strip() == "":
            raise ValueError("El ID del servicio no puede estar vacío.")
        if not id_servicio.startswith("SERV_"):
            raise ValueError("El ID del servicio debe comenzar con 'SERV_'.")
        if len(id_servicio) > 10:
            raise ValueError("El ID del servicio no puede exceder los 10 caracteres.")
        if not descripcion_servicio or descripcion_servicio.strip() == "":
            raise ValueError("La descripción del servicio no puede estar vacía.")
        if not id_doctor or id_doctor.strip() == "":
            raise ValueError("El servicio debe estar asociado a un doctor (idDoctor vacío).")
 
        self.id_servicio = id_servicio
        self.descripcion_servicio = descripcion_servicio.strip()
        self.id_doctor = id_doctor.strip()
 
    def validacion_servicio(self):
        # Punto de extensión para reglas de negocio adicionales sobre el servicio
        return True