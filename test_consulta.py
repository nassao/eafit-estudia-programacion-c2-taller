"""Pruebas aisladas: las respuestas preparadas no acreditan una conexión real."""
from unittest.mock import Mock
from consulta import consultar_cupos


def test_consulta_con_datos():
    # Preparar: este sustituto devuelve 12 cada vez que se lo llama.
    consultar = Mock(return_value=12)
    # Actuar y comprobar: contrastamos la respuesta con la regla esperada.
    assert consultar_cupos("Python inicial", consultar) == "Python inicial: 12 cupos disponibles"
    # Verificamos también cuántas veces se consultó y con qué nombre.
    consultar.assert_called_once_with("Python inicial")


def test_consulta_sin_cupos():
    # Preparar: cero cupos es un dato, no un error.
    consultar = Mock(return_value=0)
    # Actuar y comprobar: contrastamos la respuesta con la regla esperada.
    assert consultar_cupos("Python inicial", consultar) == "Python inicial: 0 cupos disponibles"
    # Verificamos también cuántas veces se consultó y con qué nombre.
    consultar.assert_called_once_with("Python inicial")


def test_consulta_con_timeout():
    # Preparar: side_effect hace que el sustituto lance la excepción.
    consultar = Mock(side_effect=TimeoutError("Servicio lento"))
    # Actuar y comprobar: contrastamos la respuesta con la regla esperada.
    assert consultar_cupos("Python inicial", consultar) == "No disponible: intenta nuevamente"
    # Verificamos también cuántas veces se consultó y con qué nombre.
    consultar.assert_called_once_with("Python inicial")
