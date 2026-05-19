import time
import functools
from typing import Optional, List, Generator
from concurrent.futures import ThreadPoolExecutor

# Decorador para medir el tiempo de ejecución de las funciones
def medir_tiempo(funcion):
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        fin = time.perf_counter()
        print(f"[⏱️] La función '{funcion.__name__}' tardó {fin - inicio:.6f} segundos en ejecutarse.")
        return resultado
    return wrapper

# Script original mejorado para contar del 1 al 2027 usando un generador y decorador
@medir_tiempo
def contar():
    """Imprime números del 1 al 2027 generados de manera eficiente."""
    def generador_numeros(limite: int) -> Generator[int, None, None]:
        for numero in range(1, limite + 1):
            yield numero

    for numero in generador_numeros(2027):
        print(numero)

class Hola:
    """Clase base que solicita nombre y edad del usuario al instanciarse."""
    def __init__(self):
        self.name = input("¿Cuál es tu nombre? ")
        try:
            self.age = int(input("¿Cuál es tu edad? "))
        except ValueError:
            self.age = None
            print("Edad no válida, se ha establecido como None.")
            
    def saludo(self):
        if self.age is not None:
            print(f"Hola {self.name}, tienes {self.age} años.")
        else:
            print(f"Hola {self.name}.")

# --- Nuevas características complejas ---

class Persona(Hola):
    """Clase avanzada que hereda de Hola y añade propiedades, métodos mágicos y validaciones."""
    
    def __init__(self):
        super().__init__()
        self._email: Optional[str] = None

    @property
    def email(self) -> Optional[str]:
        return self._email

    @email.setter
    def email(self, valor: str):
        if "@" in valor and "." in valor:
            self._email = valor
        else:
            raise ValueError("Formato de correo electrónico inválido.")

    def __str__(self) -> str:
        edad_str = f"{self.age} años" if self.age is not None else "edad desconocida"
        email_str = f", Email: {self._email}" if self._email else ""
        return f"[Persona] Nombre: {self.name}, Edad: {edad_str}{email_str}"

    def __repr__(self) -> str:
        return f"Persona(name='{self.name}', age={self.age}, email='{self._email}')"


class ProcesadorNumerico:
    """Clase compleja que realiza procesamiento concurrente de datos numéricos."""
    
    @staticmethod
    def es_primo(n: int) -> bool:
        """Determina si un número es primo."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @medir_tiempo
    def procesar_primos_concurrente(self, numeros: List[int]) -> List[int]:
        """Filtra números primos usando un grupo de hilos (ThreadPoolExecutor) para mayor eficiencia."""
        print(f"\n[🚀] Iniciando procesamiento concurrente de {len(numeros)} números...")
        with ThreadPoolExecutor() as ejecutor:
            # Map evalúa la función es_primo en paralelo sobre la lista de números
            resultados = list(ejecutor.map(self.es_primo, numeros))
        
        primos = [num for num, es_primo in zip(numeros, resultados) if es_primo]
        return primos

if __name__ == "__main__":
    print("--- 1. Ejecución del Contador Original (Optimizado con Generadores) ---")
    contar()
    
    print("\n--- 2. Interacción con la clase avanzada Persona (Herencia y Encapsulamiento) ---")
    persona = Persona()
    persona.saludo()
    
    # Solicitar email adicional para demostrar propiedades y setters
    try:
        correo = input("Introduce tu correo electrónico: ")
        persona.email = correo
        print(f"Correo registrado con éxito.")
    except ValueError as e:
        print(f"Error: {e}")
        
    print(f"\nRepresentación en texto (__str__): {persona}")
    print(f"Representación técnica (__repr__): {repr(persona)}")
    
    print("\n--- 3. Demostración de Procesamiento Concurrente (ThreadPoolExecutor) ---")
    # Generamos una lista de números para evaluar cuáles son primos
    lista_numeros = list(range(100, 150))
    procesador = ProcesadorNumerico()
    primos_encontrados = procesador.procesar_primos_concurrente(lista_numeros)
    print(f"Números primos encontrados entre 100 y 150: {primos_encontrados}")
