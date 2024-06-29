# app/utils.py

from app.db import db
from app.models import Persona
from datetime import datetime

def log_consulta(parametros, resultado):
    from app.models import db, RegistroConsulta

    print(f"Guardando consulta: {parametros} - {resultado}")

    nueva_consulta = RegistroConsulta(
        fecha_consulta=datetime.now(),
        parametros_busqueda=parametros,
        resultado=resultado
    )
    
    db.session.add(nueva_consulta)
    db.session.commit()


def calcular_edad(fecha_nacimiento):
    # Calcula la edad a partir de la fecha de nacimiento
    hoy = datetime.today()
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def formatear_nombre(nombre):
    # Formatea el nombre capitalizando la primera letra de cada palabra
    nombre_formateado = ' '.join(word.capitalize() for word in nombre.split())
    return nombre_formateado
