"""Casos de referencia para conservar comportamiento al mejorar la legibilidad."""
from ejemplo_calidad import clasificar_cancelacion


def test_cancelacion_total():
    assert clasificar_cancelacion(4, 4) == "total"


def test_cancelacion_parcial():
    assert clasificar_cancelacion(2, 4) == "parcial"


def test_cancelacion_excesiva():
    assert clasificar_cancelacion(5, 4) == "excesiva"


def test_cancelacion_cero():
    assert clasificar_cancelacion(0, 4) == "no positiva"


def test_cancelacion_negativa():
    assert clasificar_cancelacion(-1, 4) == "no positiva"
