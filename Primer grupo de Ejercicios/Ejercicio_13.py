'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''
import math
def es_primo(num) :
  if num <= 1 :
    return False
  if num <= 3 :
    return True
  if num % 2 == 0 or num % 3 == 0 :
    return False
  for i in range(5, int(math.sqrt(num)) + 1, 6):
    if num % i == 0 or num % (i + 2) == 0:
      return False
  return True

while True :
  num_str = input ('Introduzca un número para saber si es primo: ')
  if num_str.isdigit() :
    num = int(num_str)
    if es_primo(num) :
      print(f'El número dado, {num_str}, es primo.')
      break
    else :
      print(f'El número dado, {num_str}, NO es primo.')
      break
  else :
    print ('Por favor, el dato introducido debe ser un número entero.')