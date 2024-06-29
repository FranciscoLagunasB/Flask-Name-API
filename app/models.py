from app.db import db
from sqlalchemy.dialects.postgresql import JSONB

class Persona(db.Model):
    __tablename__ = 'personas'

    persona_id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(100), nullable=False)

class RegistroConsulta(db.Model):
    __tablename__ = 'registro_consultas'

    consulta_id = db.Column(db.Integer, primary_key=True)
    fecha_consulta = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    parametros_busqueda = db.Column(JSONB, nullable=False)
    resultado = db.Column(JSONB, nullable=False)