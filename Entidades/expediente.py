from datetime import date


class Expediente:
    def __init__(self, id_expediente: str, fecha_apertura: date, alergias_medicamentos: str,
                 enfermedades_preexistentes: str, notas_medicas: str, historial_citas: list = None):
        
        # El ID debe iniciar con "EXP_" y no exceder 10 caracteres
        
        if not id_expediente or id_expediente.strip() == "":
            raise ValueError("El ID del expediente no puede estar vacío.")
        if not id_expediente.startswith("EXP_"):
            raise ValueError("El ID del expediente debe comenzar con 'EXP_'.")
        if len(id_expediente) > 10:
            raise ValueError("El ID del expediente no puede exceder los 10 caracteres.")
        if not isinstance(fecha_apertura, date):
            raise ValueError("La fecha de apertura debe ser un objeto de tipo date.")
        if fecha_apertura > date.today():
            raise ValueError("La fecha de apertura no puede ser una fecha futura.")
        if alergias_medicamentos is None:
            raise ValueError("El campo de alergias no puede ser nulo (use cadena vacía si no aplica).")
        if enfermedades_preexistentes is None:
            raise ValueError("El campo de enfermedades preexistentes no puede ser nulo (use cadena vacía si no aplica).")
        if not notas_medicas or notas_medicas.strip() == "":
            raise ValueError("Las notas médicas no pueden estar vacías.")
        if historial_citas is not None and not isinstance(historial_citas, list):
            raise ValueError("El historial de citas debe ser una lista.")
 
        self.id_expediente = id_expediente
        self.fecha_apertura = fecha_apertura
        self.alergias_medicamentos = alergias_medicamentos.strip()
        self.enfermedades_preexistentes = enfermedades_preexistentes.strip()
        self.notas_medicas = notas_medicas.strip()
        self.historial_citas = historial_citas if historial_citas is not None else []
 
    def validacion_expediente(self):
        return True