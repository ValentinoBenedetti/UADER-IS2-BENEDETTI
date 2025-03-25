#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self, min_value=1, max_value=1):
        """Inicializa los valores mínimo y máximo del rango para calcular los factoriales."""
        self.min_value = min_value
        self.max_value = max_value

    def factorial(self, num): 
        """Calcula el factorial de un número."""
        if num < 0: 
            print("El factorial de un número negativo no existe.")
            return 0
        elif num == 0: 
            return 1
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 

    def run(self):
        """Calcula los factoriales entre min_value y max_value y los muestra."""
        if self.min_value > self.max_value:
            print("El valor de 'min' no puede ser mayor que 'max'.")
            return
        
        for num in range(self.min_value, self.max_value + 1):
            print(f"El factorial de {num} es {self.factorial(num)}")


# Verificar si se pasó un rango como argumento
if __name__ == "__main__":
    import sys

    # Si no se pasó ningún argumento
    if len(sys.argv) == 1:
        print("Debe informar un rango (inicio-fin)! Lo solicitaré ahora.")
        rango = input("Por favor, ingrese el rango de números (ej. -10 o 5-): ")

        if '-' in rango:
            if rango.startswith('-'):
                # Si el argumento es -hasta
                try:
                    fin = int(rango[1:])
                    factorial_obj = Factorial(1, fin)
                    factorial_obj.run()
                except ValueError:
                    print("Formato de rango inválido. Debe ser '-hasta'.")
            elif rango.endswith('-'):
                # Si el argumento es desde-
                try:
                    inicio = int(rango[:-1])
                    factorial_obj = Factorial(inicio, 60)
                    factorial_obj.run()
                except ValueError:
                    print("Formato de rango inválido. Debe ser 'desde-'.")
            else:
                print("Formato de rango inválido. Debe ser '-hasta' o 'desde-'.")
        else:
            print("Debe usar el formato '-hasta' o 'desde-' para el rango.")
    else:
        # Si se pasó un rango como argumento
        if '-' in sys.argv[1]:
            rango = sys.argv[1]
            if rango.startswith('-'):
                # Si el argumento es -hasta
                try:
                    fin = int(rango[1:])
                    factorial_obj = Factorial(1, fin)
                    factorial_obj.run()
                except ValueError:
                    print("Formato de rango inválido. Debe ser '-hasta'.")
            elif rango.endswith('-'):
                # Si el argumento es desde-
                try:
                    inicio = int(rango[:-1])
                    factorial_obj = Factorial(inicio, 60)
                    factorial_obj.run()
                except ValueError:
                    print("Formato de rango inválido. Debe ser 'desde-'.")
            else:
                print("Formato de rango inválido. Debe ser '-hasta' o 'desde-'.")
        else:
            print("Debe usar el formato '-hasta' o 'desde-' para el rango.")
