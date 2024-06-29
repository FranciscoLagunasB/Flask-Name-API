import pytest
from app.models import Persona, RegistroConsulta
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_crear_persona(app):
    with app.app_context():
        persona = Persona(nombre_completo='Juan Pérez')
        assert persona.nombre_completo == 'Juan Pérez'

def test_crear_registro_consulta(app):
    with app.app_context():
        consulta = RegistroConsulta(parametros_busqueda={'nombre': 'Juan Pérez'}, resultado={'encontrado': True})
        assert consulta.parametros_busqueda == {'nombre': 'Juan Pérez'}
        assert consulta.resultado == {'encontrado': True}

def test_guardar_persona_en_db(app):
    with app.app_context():
        persona = Persona(nombre_completo='María López')
        db.session.add(persona)
        db.session.commit()
        assert persona.persona_id is not None
        assert Persona.query.filter_by(nombre_completo='María López').first() is not None
