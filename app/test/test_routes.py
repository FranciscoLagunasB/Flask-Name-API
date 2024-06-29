import json
import pytest
from app import create_app
from app.models import Persona
from app.db import db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        # Aquí puedes agregar datos de prueba si es necesario
        persona = Persona(nombre_completo='Juan Pérez')
        db.session.add(persona)
        db.session.commit()

    with app.test_client() as client:
        yield client

def test_buscar_persona_encontrada(client):
    # Hacer la solicitud POST a /buscar_persona
    response = client.post('/buscar_persona', json={'nombre': 'Juan Pérez'})
    data = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert data['encontrado'] == True

def test_buscar_persona_no_encontrada(client):
    # Hacer la solicitud POST a /buscar_persona con nombre no existente
    response = client.post('/buscar_persona', json={'nombre': 'María López'})
    data = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 404
    assert data['encontrado'] == False
