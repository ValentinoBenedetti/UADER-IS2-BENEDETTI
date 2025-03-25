#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
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

# Función para manejar el rango de números
def calcular_factoriales_en_rango(inicio, fin):
    if inicio > fin:
        print("El valor de 'inicio' no puede ser mayor que 'fin'.")
        return
    
    for num in range(inicio, fin + 1):
        print(f"El factorial de {num} es {factorial(num)}")

# Verificar si se pasó un rango como argumento
if len(sys.argv) == 1:  # Si no se pasó ningún argumento
    print("Debe informar un rango (inicio-fin)! Lo solicitaré ahora.")
    rango = input("Por favor, ingrese el rango de números (ej. -10 o 5-): ")

    if '-' in rango:
        if rango.startswith('-'):
            # Si el argumento es -hasta
            try:
                fin = int(rango[1:])
                calcular_factoriales_en_rango(1, fin)
            except ValueError:
                print("Formato de rango inválido. Debe ser '-hasta'.")
        elif rango.endswith('-'):
            # Si el argumento es desde-
            try:
                inicio = int(rango[:-1])
                calcular_factoriales_en_rango(inicio, 60)
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
                calcular_factoriales_en_rango(1, fin)
            except ValueError:
                print("Formato de rango inválido. Debe ser '-hasta'.")
        elif rango.endswith('-'):
            # Si el argumento es desde-
            try:
                inicio = int(rango[:-1])
                calcular_factoriales_en_rango(inicio, 60)
            except ValueError:
                print("Formato de rango inválido. Debe ser 'desde-'.")
        else:
            print("Formato de rango inválido. Debe ser '-hasta' o 'desde-'.")
    else:
        print("Debe usar el formato '-hasta' o 'desde-' para el rango.")
