'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
'''
def bisiesto (anyo) : # Retornamos True o False en caso de que sea o no bisiesto
  if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0) :
    return True
  else :
    return False

while True :
  anyo_str = input('Introduzca un año para saber si es bisiesto: ')
  if anyo_str.isdigit() : # Por si el usuario no sabe que el año se escribe con números e inserta letras...
    anyo = int(anyo_str)
    if bisiesto(anyo) :
      print (f'El año introducido, {anyo_str}, es bisiesto.')
      break
    else :
      print (f'El año introducido, {anyo_str}, NO es bisiesto.')
      break
  else :
    print('Por favor, introduzca un dato correcto.')
    print()