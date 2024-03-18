'''
Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.
'''
def cal_area (base,altura) : #Función para calcular el área
  area = base * altura
  return area
def is_float(x) : #Función para comprobar si se puede pasar a float
  try :
    float (x)
    return True
  except :
    return False
print()
print('Para conocer el área del rectángulo en cuestión debe ingresar los siguientes datos: ')
while True :
  base = input('Ingrese la "Base" del rectángulo: ')
  altura = input('Ingrese la "altura" del rectángulo: ')
  print()
  if is_float(base) and is_float(altura): #Si pueden pasarse ambos a float se convierten y se imprime el área tras el cálculo
    base = float(base)
    altura = float(altura)
    resultado = cal_area (base,altura)
    print (f'El Área del rectángulo, siendo su base de {base} y su altura de {altura} es {resultado}')
    break
  else : #Si no se pide al usuario que repita la inserción de datos
    print ('Por favor, ingrese los datos numéricos de manera correcta')