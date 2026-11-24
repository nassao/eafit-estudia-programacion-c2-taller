"""Ejecutar con python demo_taller.py para conectar con el encuentro anterior."""
from taller import Taller


def main():
    # Cada caso empieza con un objeto nuevo: las operaciones no se acumulan.
    for cantidad in (3, 13, 12):
        taller = Taller("Python inicial", 16, 4)
        resultado = taller.inscribir(cantidad)
        print(f"Inscribir {cantidad}: {resultado}; inscritos={taller.inscritos}")


# Importar este módulo no ejecuta la demostración; ejecutarlo como archivo sí.
if __name__ == "__main__":
    main()
