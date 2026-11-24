"""Ejemplo de fixture con limpieza de un recurso en memoria."""
import pytest
from io import StringIO


@pytest.fixture
def registro():
    # Preparar: StringIO se usa como un archivo, pero vive en memoria.
    recurso = StringIO()
    print("Preparación: abrir registro en memoria")
    # Entregar el recurso a la prueba; pytest retoma aquí cuando termina.
    yield recurso
    # Limpiar: cerrar incluso si una aserción de la prueba falla.
    recurso.close()
    print("Limpieza: cerrar registro en memoria")


def test_registro(registro):
    # Actuar: escribir. Comprobar: leer el contenido que quedó almacenado.
    registro.write("inscripción aceptada")
    assert registro.getvalue() == "inscripción aceptada"
