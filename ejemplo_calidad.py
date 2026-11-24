"""Misma clasificación, con menos anidación y las mismas tres decisiones."""


def clasificar_cancelacion(cantidad, inscritos):
    """Entradas enteras; devuelve una categoría, sin cambiar el estado."""
    if cantidad <= 0:
        return "no positiva"
    if cantidad > inscritos:
        return "excesiva"
    if cantidad == inscritos:
        return "total"
    return "parcial"
