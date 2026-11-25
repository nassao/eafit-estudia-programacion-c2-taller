"""Regla de inscripción: validar primero y cambiar el estado solo al aceptar."""


class Taller:
    """Representa un taller con capacidad fija y una cantidad de inscritos."""

    def __init__(self, nombre, cupo, inscritos=0):
        # Un cupo cuenta personas completas. type(...) is int también excluye
        # True y False, que Python considera subclases de los enteros.
        if type(cupo) is not int or cupo <= 0:
            raise ValueError("El cupo debe ser entero y positivo")
        self.nombre = nombre
        self._cupo = cupo
        # Usamos la propiedad: el estado inicial pasa por la misma validación
        # que una asignación posterior. No escribimos _inscritos directamente.
        self.inscritos = inscritos

    @property
    def cupo(self):
        """Permite leer el cupo; no ofrece un setter para cambiarlo."""
        return self._cupo

    @property
    def inscritos(self):
        """Expone el valor almacenado en el atributo interno _inscritos."""
        return self._inscritos

    @inscritos.setter
    def inscritos(self, valor):
        # Invariante: el estado siempre debe estar entre cero y el cupo.
        # Si lanzamos la excepción, la asignación de abajo nunca se ejecuta.
        if type(valor) is not int or not 0 <= valor <= self.cupo:
            raise ValueError("Los inscritos deben ser enteros entre cero y el cupo")
        self._inscritos = valor

    def inscribir(self, cantidad):
        """Devuelve un resultado de negocio o lanza ValueError por tipo inválido."""
        # Una cantidad de otro tipo es un dato inválido para esta operación.
        if type(cantidad) is not int:
            raise ValueError("La cantidad debe ser entera")
        # Estos rechazos son resultados normales de la regla. Cada return
        # termina el método antes de cambiar el número de inscritos.
        if cantidad <= 0:
            return "Rechazado: cantidad no positiva"
        if self.inscritos + cantidad > self.cupo:
            return "Rechazado: cupo insuficiente"
        # Solo llegamos aquí si todas las condiciones anteriores se cumplen.
        # += lee la propiedad, suma y vuelve a pasar por su setter.
        self.inscritos += cantidad
        return "Aceptado"

# PASO 2: descomenta solo el código entre los marcadores VERDE.
# PASO 3: comenta de nuevo VERDE y descomenta REFACTOR.
# Mantén como máximo una definición activa de cancelar.

# >>> VERDE: INICIO DEL BLOQUE

    def cancelar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.inscritos:
                self.inscritos -= cantidad
                return "Aceptado"
            else:
                return "Rechazado: inscritos insuficientes"
        else:
            return "Rechazado: cantidad no positiva"

#     def cancelar(self, cantidad):
#         """Cancela una cantidad válida; conserva inscritos cuando rechaza."""
#         # Primero distinguimos el tipo; luego validamos la regla de negocio.
#         if type(cantidad) is int:
#             if cantidad > 0:
#                 if cantidad <= self.inscritos:
#                     self.inscritos -= cantidad
#                     return "Aceptado"
#                 else:
#                     return "Rechazado: inscritos insuficientes"
#             else:
#                 return "Rechazado: cantidad no positiva"
#         else:
#             raise ValueError("La cantidad debe ser entera")
# <<< VERDE: FIN DEL BLOQUE

# >>> REFACTOR: INICIO DEL BLOQUE
#     def cancelar(self, cantidad):
#         """Retira inscritos solo después de validar el tipo y la regla de negocio."""
#         if type(cantidad) is not int:
#             raise ValueError("La cantidad debe ser entera")
#         if cantidad <= 0:
#             return "Rechazado: cantidad no positiva"
#         if cantidad > self.inscritos:
#             return "Rechazado: inscritos insuficientes"
#         # La resta usa el setter: el estado se mantiene entre cero y el cupo.
#         self.inscritos -= cantidad
#         return "Aceptado"
# <<< REFACTOR: FIN DEL BLOQUE
