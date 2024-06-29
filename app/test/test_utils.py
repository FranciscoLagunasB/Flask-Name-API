import pytest
from app.utils import calcular_edad, formatear_nombre
from unittest.mock import patch

def test_calcular_edad():
    edad = calcular_edad('1990-01-01')
    assert edad == 34  # Ajustar la edad según la fecha actual y la fecha de nacimiento proporcionada

def test_formatear_nombre():
    nombre_formateado = formatear_nombre('juan pÉrEz')
    assert nombre_formateado == 'Juan Pérez'