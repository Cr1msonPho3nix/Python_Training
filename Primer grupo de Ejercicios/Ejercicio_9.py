'''
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
'''
def conversor_DOL_a_EUR (x) :
  resultado = x * 0.85
  return resultado
def is_float(x) :
  try :
    float (x)
    return True
  except :
    return False

print('Bienvenidos al convertidor de "Dólares" a "Euros" (Actualmente la tasa de cambio es de 1 Dólar a 0.85 Euros).')
while True :
  euros = input('Introduzca la cantidad que quiere convertir (Decimales con ".", por ejemplo 5.87): ')
  if not is_float(euros) :
    print ('Introduzca una cantidad válida.')
  else :
    euros = float(euros)
    resultado = conversor_DOL_a_EUR (euros)
    print (f'La cantidad de {euros}$ sería equivalente a {resultado}€.')
    break