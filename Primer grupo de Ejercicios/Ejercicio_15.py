'''
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''
200
def min_a_horas (number) :
  horas = number // 60
  minutos = number - (horas * 60)
  h_m = [horas,minutos]
  return h_m

while True :
  minutos_str = input('Por favor, introduzca los minutos que serán pasados a horas y minutos: ')
  if minutos_str.isdigit() :
    minutos = int(minutos_str)
    horas_mins = min_a_horas(minutos)
    print (f'Los minutos introducidos, {minutos_str}, equivaldrían a {horas_mins[0]} horas y {horas_mins[1]} minutos.')
    break
  else :
    print('Por favor introduzca un número válido.')