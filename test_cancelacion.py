"""Pruebas preparadas para activar el paso ROJO del taller."""
# INICIO: deja el bloque comentado; las otras 16 pruebas ya se ejecutan.
# PASO 1: selecciona solo el código entre los marcadores y quita sus comentarios.
# No cambies los esperados para obtener verde. Las seis pruebas comparten el contrato.

# >>> ROJO: INICIO DEL BLOQUE
import pytest
from taller import Taller


@pytest.fixture
def taller():
    # La fixture es local a este archivo; no depende de test_taller.py.
    return Taller("Python", 16, 4)


def test_cancelar_parcial(taller):
    assert taller.cancelar(2) == "Aceptado"
    assert taller.inscritos == 2


def test_cancelar_exceso(taller):
    assert taller.cancelar(5) == "Rechazado: inscritos insuficientes"
    assert taller.inscritos == 4


def test_cancelar_total(taller):
    assert taller.cancelar(4) == "Aceptado"
    assert taller.inscritos == 0


def test_cancelar_cero(taller):
    assert taller.cancelar(0) == "Rechazado: cantidad no positiva"
    assert taller.inscritos == 4


def test_cancelar_negativo(taller):
    assert taller.cancelar(-1) == "Rechazado: cantidad no positiva"
    assert taller.inscritos == 4


def test_cancelar_tipo_invalido(taller):
    with pytest.raises(ValueError, match="La cantidad debe ser entera"):
        taller.cancelar("2")
    assert taller.inscritos == 4
# <<< ROJO: FIN DEL BLOQUE

def test_crear_con_tipo_invalido():
    with pytest.raises(ValueError, match="El cupo debe ser entero y positivo"):
        Taller("Python", "16", 4)
    with pytest.raises(ValueError, match="El cupo debe ser entero y positivo"):
        Taller("Python", True, 4)
    with pytest.raises(ValueError, match="El cupo debe ser entero y positivo"):
        Taller("Python", {}, 4)

def test_cancelar_en_vacio():
    taller = Taller("Python", 16, 0)
    assert taller.cancelar(0) == "Rechazado: cantidad no positiva"
    assert taller.inscritos == 0

