'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''
def conteo (lista) : # Función para contar pares e impares
  cont_pair = 0
  cont_odd = 0
  for number in lista :
    if number % 2 == 0 :
      cont_pair += 1
    elif not number % 2 == 0 :
      cont_odd += 1
  return cont_pair, cont_odd

print ('Introduzca una serie de números para saber cuántos son pares e i. Para dejar de añadir números, inserte "x":')
list = []
while True : # Bucle para que el programa se repita hasta que el ususario lo pare
  num_str = input ('Inserte un número entero o inserte "X" si no quiere insertar más números: ')
  if num_str.lower() == 'x':
    if len(list) == 0 : # Si el usuario pone x, pero no hay nada en la lista, pone el mensaje
      print ('No ha insertado ningún número...')
    else : # Si hay algo en la lista hace la operación y devuelve el resultado
      pair_num, odd_num = conteo(list)
      print (f'De la lista de números que ha introducido, "{list}", {pair_num} es/son pares y {odd_num} es/son impares.')
      break
  elif num_str.isdigit() : # Si el número es un entero lo mete en la lista
    num = int(num_str)
    list.append(num)
    print (f'Número {num} añadido a la lista.')
  else :
    print('Por favor, introduzca un número entero válido.')