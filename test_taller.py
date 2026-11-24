"""Pruebas finales: pytest inyecta un Taller nuevo en cada caso que lo solicita."""
import pytest
from taller import Taller


# Preparar: pytest identifica esta fábrica por su decorador y por el nombre
# del parámetro que solicitan las pruebas. No se llama manualmente.
@pytest.fixture
def taller():
    # Alcance predeterminado: una instancia nueva para cada prueba.
    return Taller("Python inicial", 16, 4)


def test_inscripcion_valida(taller):
    # Actuar: inscribir tres. Comprobar: mensaje y estado, calculado desde 4 + 3.
    mensaje = taller.inscribir(3)
    assert mensaje == "Aceptado"
    assert taller.inscritos == 7


def test_inscripcion_excesiva(taller):
    # El total sería 17. El rechazo debe conservar los cuatro inscritos.
    assert taller.inscribir(13) == "Rechazado: cupo insuficiente"
    assert taller.inscritos == 4


def test_asignacion_negativa(taller):
    # raises exige la excepción dentro del bloque; después comprobamos el estado.
    with pytest.raises(ValueError, match="enteros entre cero y el cupo"):
        taller.inscritos = -1
    assert taller.inscritos == 4


def test_estado_inicial_negativo():
    # El constructor también debe proteger la regla, antes de tener un objeto válido.
    with pytest.raises(ValueError):
        Taller("Python inicial", 16, -1)


def test_inscribir_cero(taller):
    # Un taller vacío es válido, pero una operación de cero inscripciones se rechaza.
    assert taller.inscribir(0) == "Rechazado: cantidad no positiva"
    assert taller.inscritos == 4


def test_asignacion_supera_cupo(taller):
    # El setter debe impedir superar el cupo incluso por asignación directa.
    with pytest.raises(ValueError):
        taller.inscritos = 17
    assert taller.inscritos == 4


def test_otro_caso_comienza_en_cuatro(taller):
    # La fixture prepara otro objeto. Llenar exactamente el cupo sí está permitido.
    assert taller.inscritos == 4
    assert taller.inscribir(12) == "Aceptado"
    assert taller.inscritos == 16
