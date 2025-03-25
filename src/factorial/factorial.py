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
    rango = input("Por favor, ingrese el rango de números (ej. 4-8): ")
    
    # Separar el rango en dos números
    try:
        inicio, fin = map(int, rango.split('-'))
        calcular_factoriales_en_rango(inicio, fin)
    except ValueError:
        print("Formato de rango inválido. Debe ser 'inicio-fin'.")
else:
    # Si se pasó un rango como argumento
    try:
        inicio, fin = map(int, sys.argv[1].split('-'))
        calcular_factoriales_en_rango(inicio, fin)
    except ValueError:
        print("Formato de rango inválido. Debe ser 'inicio-fin'.")
