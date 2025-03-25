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

# Verificar si se pasó un número como argumento
if len(sys.argv) == 1:  # Si no se pasó ningún número como argumento
    print("Debe informar un número! Lo solicitaré ahora.")
    num = int(input("Por favor, ingrese un número: "))  # Solicitar al usuario el número
else:
    num = int(sys.argv[1])  # Usar el número pasado como argumento

print(f"El factorial de {num} es {factorial(num)}")
