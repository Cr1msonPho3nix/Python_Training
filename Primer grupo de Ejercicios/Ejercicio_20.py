'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario
'''
def sumar_lista (lista) : # Función para contar pares e impares
  suma = 0
  for number in lista :
    suma = suma + number
  return suma
def is_float(x) : #Función para comprobar si se puede pasar a float
  try :
    float (x)
    return True
  except :
    return False

print ('Introduzca una serie de números para saber la suma total de dichos números. Cuando termine de introducir números, inserte "x":')
list = []
while True : # Bucle para que el programa se repita hasta que el ususario lo pare
  num_str = input ('Inserte un número entero o inserte "X" si no quiere insertar más números: ')
  if num_str.lower() == 'x':
    if len(list) == 0 : # Si el usuario pone x, pero no hay nada en la lista, pone el mensaje
      print ('No ha insertado ningún número...')
    else : # Si hay algo en la lista hace la operación y devuelve el resultado
      total = sumar_lista(list)
      print (f'La suma de la lista de números que ha introducido, "{list}", es: {total}.')
      break
  elif num_str.isdigit():
    num = int(num_str)
    list.append(num)
    print (f'Número {num} añadido a la lista.')
  elif is_float(num_str) :
    num = float(num_str)
    list.append(num)
    print (f'Número {num} añadido a la lista.')
  else :
    print('Por favor, introduzca un dato válido.')