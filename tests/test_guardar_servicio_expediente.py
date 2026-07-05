from datetime import date
from pathlib import Path
import json
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from Entidades.servicio import Servicio
from Entidades.expediente import Expediente


def guardar_json(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)


def cargar_json(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)


if __name__ == '__main__':
    servicio = Servicio('SERV_001', 'Limpieza dental', 'DOC_001')
    expediente = Expediente('EXP_001', date(2026, 7, 1), 'Penicilina', 'Ninguna', 'Paciente estable')

    ruta_servicios = Path('tests/servicios.json')
    ruta_expedientes = Path('tests/expedientes.json')

    guardar_json(ruta_servicios, [
        {
            'id_servicio': servicio.id_servicio,
            'descripcion_servicio': servicio.descripcion_servicio,
            'id_doctor': servicio.id_doctor,
        }
    ])

    guardar_json(ruta_expedientes, [
        {
            'id_expediente': expediente.id_expediente,
            'fecha_apertura': expediente.fecha_apertura.isoformat(),
            'alergias_medicamentos': expediente.alergias_medicamentos,
            'enfermedades_preexistentes': expediente.enfermedades_preexistentes,
            'notas_medicas': expediente.notas_medicas,
            'historial_citas': expediente.historial_citas,
        }
    ])

    print('Servicio guardado:', cargar_json(ruta_servicios))
    print('Expediente guardado:', cargar_json(ruta_expedientes))
