'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
def imc_calc (kg,m) : #Fórmula para calcular el IMC
  imc = kg/(m**2)
  return imc

print('Bienvenidos al conversor de Índice de Masa Corporal.')
while True :
  print()
  kilos = input('Introduzca tu peso, por favor: ')
  altura = input('Introduzca su altura (Utilizar "." para decimales): ')
  def is_float(x) :
    try :
      float (x)
      return True
    except :
      return False
  if is_float(kilos) and is_float(altura) :
    kilos = float(kilos)
    altura = float (altura)
    if kilos < 10 or altura > 3 :
      print ('Los datos introducidos son incorrectos.')
    else :
      resultado = imc_calc(kilos,altura)
      resultado = round (resultado,1)
      print(f'Su Índice de Masa Corporal (IMC) es {resultado}.')
      break
  else :
    print ('Alguno de los datos introducidos es incorrecto. Por favor, inténtelo de nuevo.')