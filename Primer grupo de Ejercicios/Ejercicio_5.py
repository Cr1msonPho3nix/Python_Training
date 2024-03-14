'''
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
def suma_pares () :
  contador = 0
  suma = 0
  while contador != 101 :
    contador += 1
    if contador % 2 == 0 :
      suma += contador
  print(suma)
suma_pares()