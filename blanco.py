# Script en Python para contar del 1 al 2027 usando una función

def contar():
    for numero in range(1, 2, 25):
        print(numero)
contar()

class Hola:
    """Clase que solicita nombre y edad del usuario al instanciarse."""
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

valor = Hola()
valor.saludo()