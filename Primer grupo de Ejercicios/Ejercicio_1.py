'''
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''
def celsius_a_farenheit (celsius) :
  farenheit = ((9/5)*celsius) + 32
  return farenheit

def conversor () :
  print('Bienvenidos al conversor de grados "Celsius" a "Farenheit"')
  selection = input('Inserte "1" para acceder al conversor o "2" para cerrar del programa: ')
  # Entra en bucle hasta que sale por comando del usuario.
  while True :
    if selection == '1' :
      print()
      celsius = input('Por favor, indique los grados Celsius que quiere convertir en números: ')
      error = False
      try :
        number = int(celsius)
      except ValueError :
        error = True
      if error == False :
        farenheint = celsius_a_farenheit(float(celsius))
        print()
        print(f'Su medida, {celsius}º Celsius,  es el equivalente a {farenheint}º Farenheint')
        exit = input ('Si quiere realizar otra conversión, pulse "1", si por el contrario quiere cerrar el programa, pulse "2": ')
        # Si el usuario quiere volver a convertir la opcion 1 no hace nada, por lo que el bucle anterior vuelve a repetirse
        if exit == '1' :
          print()
          pass
        elif  exit == '2':
          print('Cerrando el conversor')
          break
        else :
          print()
          print('Por favor, seleccione la opción "1" o "2".')
          selection = input('Si quiere realizar otra conversión, pulse "1", si por el contrario quiere cerrar el programa, pulse "2": ')
          print()
      else :
        print('Por favor, introduzca un número válido.')
    elif  selection == '2':
      print('Cerrando el conversor')
      break
    else :
      print ('Por favor, seleccione la opción "1" o "2".')

conversor()