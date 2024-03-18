'''
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''
def descuento_20 (precio) :
  resultado = precio - (precio * 0.20)
  return resultado
def is_float(x) :
  try :
    float (x)
    return True
  except :
    return False

while True :
  precio_str = input ('Introduzca el precio al que aplicar el 20% de descuento (Ejemplo: 12.50): ')
  if is_float(precio_str) :
    precio = float(precio_str)
    if not precio <= 0 :
      precio_descuento = descuento_20(precio)
      precio_descuento = round (precio_descuento,2)
      print (f'El precio introducido, {precio_str}€, quedaría en {precio_descuento}€ con el 20% de descuento incluido.')
      break
    else :
      print ('El precio no puede ser "cero" o negativo.')
  else :
    print ('Por favor, introduzca un dato válido.')