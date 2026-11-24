"""Lógica de presentación de cupos, separada de cómo se obtienen los datos."""


def consultar_cupos(nombre, consultar):
    # Recibimos una función como argumento. En pruebas podemos entregar un
    # sustituto controlado; este módulo no implementa ninguna conexión de red.
    try:
        disponibles = consultar(nombre)
    except TimeoutError:
        # Solo manejamos este error conocido. Otros errores no se ocultan.
        return "No disponible: intenta nuevamente"
    # Cero es una respuesta válida: no lo confundimos con falta de respuesta.
    return f"{nombre}: {disponibles} cupos disponibles"
