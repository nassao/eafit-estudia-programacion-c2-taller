# Taller de Python · EAFIT EstudIA · Capa 2

Ejercicio de clase preparado por Daniel Ramírez: un taller con 16 cupos, inscripciones y pruebas con pytest. Este es un repositorio docente de práctica, no un repositorio institucional administrado por EAFIT.

## Objetivo

Ver cómo una expectativa nueva produce una prueba fallida, cómo el código la satisface y cómo una refactorización conserva el comportamiento. El escenario está guardado en **verde inicial**. Las pruebas y alternativas de cancelar están comentadas, listas para activarse desde PyCharm o VS Code.

## Preparación local

Abre la raíz del proyecto. Crea y selecciona `.venv` con Python 3.10 o posterior; Actions usa Python 3.14.

Windows / PowerShell:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Instala las herramientas:
```bash
python -m pip install -r requirements.txt
```
En VS Code usa **Python: Select Interpreter**; en PyCharm selecciona el intérprete de `.venv` para el proyecto. Ejecuta los comandos desde la terminal de esa carpeta.

## Secuencia de la demostración

| Paso | Cambio local | Resultado esperado de pytest |
|---|---|---|
| 0 · Verde inicial | Ninguno; cancelar y sus pruebas están comentados | 16 passed |
| 1 · Rojo | Activar el bloque ROJO de test_cancelacion.py | 6 failed, 16 passed: falta cancelar |
| 2 · Verde | Activar el bloque VERDE de taller.py | 22 passed |
| 3 · Refactor | Comentar VERDE y activar REFACTOR en taller.py | 22 passed |

**Selecciona únicamente las líneas de código entre los marcadores**, sin incluir las líneas `>>>` y `<<<`. Usa la acción del editor para alternar comentarios de línea. Al quitar `# `, conserva la indentación de Python. En taller.py los métodos pertenecen a la clase Taller. No actives las dos versiones a la vez: Python conservaría la última definición y ocultaría la comparación.

Después de cada cambio, guarda y ejecuta:
```bash
python -m pytest -q --cov=taller --cov-branch --cov-report=term-missing
python -m ruff check .
```
En rojo, lee los seis AttributeError: las pruebas se recogieron, pero el método aún no existe. Un error de sintaxis o importación no es el fallo buscado.

En verde, comprueba mensaje/excepción y estado final para cada caso. En refactor, las salidas tempranas reducen anidación; no cambia el contrato ni se afirma que disminuya el número de decisiones. No hace falta recuperar commits ni cambiar ramas para recorrer los pasos.

## GitHub Actions

El workflow `.github/workflows/pruebas.yml` se activa al recibir un push. Obtiene el código, prepara Python, instala las dependencias, ejecuta pruebas con cobertura y revisa el código con Ruff.

Para observar cada paso en GitHub: guarda, ejecuta localmente, registra un commit desde tu IDE y envíalo con push. En **Actions > Pruebas del taller**, abre la ejecución de ese commit y el job **verificar**. Si fallan las pruebas, Ruff se omite en ese workflow; eso no demuestra que Ruff haya pasado.

Mensajes sugeridos, en orden:
- `Prueba: definir cancelaciones del taller`
- `Implementar cancelaciones del taller`
- `Refactorizar cancelaciones con salidas tempranas`

Un commit registra los cambios y un push los envía. No necesitas desplazarte a versiones anteriores. La ejecución inicial solo acredita las 16 pruebas activas: todavía no comprueba cancelar. Las alternativas comentadas son un apoyo temporal para esta clase.

También se puede iniciar **Run workflow** para repetir el código ya publicado; no ejecuta los cambios que aún estén solamente en tu equipo.
