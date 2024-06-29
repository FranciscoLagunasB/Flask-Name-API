# app/routes.py

from flask import Blueprint, request, jsonify
from sqlalchemy import func
from app.db import db
from app.models import Persona
from app.utils import log_consulta

bp = Blueprint('main', __name__)

@bp.route('/buscar_persona', methods=['POST'])
def buscar_persona():
    data = request.get_json()
    nombre = data.get('nombre', '').strip()

    print(nombre)

    if not nombre:
        return jsonify({'encontrado': False}), 400

    persona_encontrada = Persona.query.filter(func.lower(Persona.nombre_completo) == func.lower(nombre)).first()
    print(persona_encontrada)

    if persona_encontrada:
        log_consulta(data, {'encontrado': True})
        return jsonify({'encontrado': True}), 200
    else:
        log_consulta(data, {'encontrado': False})
        return jsonify({'encontrado': False}), 404