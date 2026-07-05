from datetime import date
import sys
import os


from doctor import Doctor
from personal_administrativo import PersonalAdministrativo
from rol import Rol
from sucursal import Sucursal
from paciente import Paciente
from servicio import Servicio
 
 
roles = []
personal = []
doctores = []
sucursales = []
 
rol1 = Rol("R01", "Administrador", "Gestiona la sucursal")
personal1 = PersonalAdministrativo("P01", "Ana Perez", rol1)
servicio1 = Servicio("S01", "Consulta General", 25.00)
paciente1 = Paciente("PA01", "Carlos Ramirez")
doctor1 = Doctor("D01", "Dra. Maria Lopez", "JVP-4521", paciente1)
sucursal1 = Sucursal("SUC01", "Clinica Central", "Santa elena", "7676-6767")
 
print(rol1.validacion_rol(roles) or "Rol tamo vien")
print(personal1.validacion_personal_admin(personal) or "Personal all good")
print(doctor1.validacion_doctor(doctores) or "Doctores all nice")
print(sucursal1.validacion_sucursal(sucursales) or "Sucursal todo correcto")
 
roles.append(rol1)
personal.append(personal1)
doctores.append(doctor1)
sucursales.append(sucursal1)
 
doctor1.crear_cita("CI01", date(2026, 7, 10), servicio1)  # fecha: YYYY, M, D
print("Citas del doctor", [c.idCita for c in doctor1.citas_doctor])
 
sucursal1.personal_admin_agregados.append(personal1)
sucursal1.doctores_agregados.append(doctor1)
print("Personal en sucursal: ", [p.idPersonalAdministrativo for p in sucursal1.personal_admin_agregados])
print("Doctores en sucursal: ", [d.idDoctor for d in sucursal1.doctores_agregados])