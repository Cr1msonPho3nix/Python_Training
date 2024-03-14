'''
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''
def propina (subtotal) :
  total = (subtotal * 0.15) + subtotal
  return total

def precio_total () :
  while True :
    print()
    precio = input('Introduzca el monto para calcular su "15%" de propina: ')
    error = False
    try :
      number = float(precio)
    except ValueError :
      error = True
    if error == False :
      total = propina(float(precio))
      print()
      print('El precio total incluyendo un "15%" de propina es: ')
      print(f'{total} €.')
      print()
      print('Gracias por usar nuestro aplicador de propinas.')
      break
    else :
      print()
      print('Por favor, introduzca una cifra válida.')
precio_total()