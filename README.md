# Instrucciones y Guía: blanco.py (Versión Avanzada)

## Descripción

Este script de Python ha sido ampliado para integrar conceptos avanzados de programación en Python, lo que lo convierte en un excelente patio de pruebas (playground) educativo y funcional.

### Componentes Principales:

#### 1. Decorador `medir_tiempo`
Un decorador que utiliza `functools.wraps` para medir con alta precisión (`time.perf_counter`) y mostrar en consola el tiempo exacto que le toma ejecutarse a cualquier función decorada.

#### 2. Función `contar()` (Optimizada con Generadores)
Imprime los números del 1 al 2027 utilizando un **Generador** de Python (`yield`). Esto optimiza el consumo de memoria del sistema al no almacenar toda la secuencia en RAM antes de imprimir. Además, está decorada con `@medir_tiempo`.

#### 3. Clases y Programación Orientada a Objetos Avanzada
- **Clase Base `Hola`**: Solicita el nombre y la edad del usuario con control de excepciones básico (`try-except` para `ValueError`).
- **Clase Heredada `Persona`**:
  - Implementa herencia mediante `super().__init__()`.
  - Incorpora propiedades encapsuladas (`@property` y `@email.setter`) para validar formatos (en este caso, validación básica del correo electrónico).
  - Define métodos mágicos estándar (`__str__` y `__repr__`) para una representación en texto enriquecida.

#### 4. Clase `ProcesadorNumerico` (Procesamiento Concurrente)
Demuestra el uso de la biblioteca estándar `concurrent.futures` mediante `ThreadPoolExecutor` para analizar la primalidad de un rango de números de forma concurrente, acelerando tareas intensivas o bloqueantes de CPU/I-O utilizando múltiples hilos.

---

## Cómo usar este script:

1. Abre una terminal o consola de comandos.
2. Navega hasta el directorio del proyecto:
   ```bash
   cd "C:\Users\josej\.gemini\antigravity\scratch\proyecto-notas"
   ```
3. Ejecuta el script con el comando:
   ```bash
   python blanco.py
   ```

---

## Estructura de la Ejecución de Muestra

Al arrancar, el script ejecutará las siguientes fases de forma secuencial:

1. **Contador Eficiente**: Imprimirá números del 1 al 2027 y mostrará la duración del proceso en microsegundos.
2. **Entrada Interactiva de Persona**:
   - Solicitará tu nombre y edad (clase base).
   - Solicitará tu correo electrónico (demostrando el setter encapsulado).
   - Imprimirá las representaciones textuales detalladas del objeto creado.
3. **Filtro Concurrente de Primos**: Analizará en paralelo un bloque de números (del 100 al 150) y mostrará únicamente los números primos detectados, calculando el tiempo de procesamiento concurrente.
