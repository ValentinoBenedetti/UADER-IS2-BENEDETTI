#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import matplotlib.pyplot as plt

# Función que calcula el número de iteraciones hasta que la secuencia llega a 1
def collatz_iterations(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Dividir entre 2 si es par
        else:
            n = 3 * n + 1  # Multiplicar por 3 y sumar 1 si es impar
        count += 1
    return count

# Lista para guardar el número de iteraciones por cada número de 1 a 10000
iterations = []
numbers = range(1, 10001)

# Calcular las iteraciones para cada número en el rango
for n in numbers:
    iterations.append(collatz_iterations(n))

# Crear el gráfico
plt.figure(figsize=(10, 6))  # Tamaño del gráfico
plt.scatter(iterations, numbers, color='blue', alpha=0.5)  # Crear el gráfico de dispersión
plt.title('Conjetura de Collatz: Número de Iteraciones por Número de Inicio')
plt.xlabel('Número de Iteraciones')  # Etiqueta para el eje X
plt.ylabel('Número de Inicio')  # Etiqueta para el eje Y
plt.grid(True)  # Mostrar la cuadrícula
plt.show()  # Mostrar el gráfico
