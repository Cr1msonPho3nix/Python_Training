'''
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.
'''
def millas_a_km (x):
  millas = x
  KILOMETROS = 1.60934
  km = millas * KILOMETROS
  return round(km,3)

def is_float(x) :
  try :
    float (x)
    return True
  except :
    return False

while True :
  print('Por favor, introduzca la distancia en "millas" que quiera convertir a "kilómetros": ')
  millas_str = input('Millas: ')
  if is_float(millas_str) :
    millas = float(millas_str)
    km = (millas_a_km(millas))
    print(f'Las millas que ha introducido, {millas_str}, equivalen a {km} kilómetros.')
    break
  else :
    print('El dato introducido es incorrecto, por favor inténtelo de nuevo introduciendo un número entero o decimal.')
    print()