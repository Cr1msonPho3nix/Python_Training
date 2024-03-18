'''
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual
'''
from datetime import datetime
def calculo_edad (nacimiento) : #Calcular la edad según la fecha actual
  fecha_actual = datetime.now()
  edad = fecha_actual.year - nacimiento.year
  if (fecha_actual.month, fecha_actual.day) < (nacimiento.month, nacimiento.day) :
    edad -= 1
  return edad

while True :
  print('Ingrese su fecha de nacimiento en introduciendo los siguientes datos: ') #Usuario introduce su edad
  dia = input ('Día de nacimiento (Ejemplo: 15)')
  mes = input ('Mes de nacimiento (Ejemplo: 05)')
  anyo = input ('Año de nacimiento (Ejemplo: 1980)')
  if anyo.isdigit() and mes.isdigit() and dia.isdigit() : #Se comprueba que los datos son numéricos, para evitar errores
    if len(dia) < 3 and len(mes) < 3 and len(anyo) < 5 :  #Se comprueba que los datos no exceden el límite, para evitar errores
      if len(dia) == 1 : #En caso de que el usuario no sepa leer y sólo ponta un dígito se le añade un 0 delante
        dia = '0' + dia
      if len(mes) == 1 :
        mes = '0' + mes
      f_nacimiento_str = f'{anyo}-{mes}-{dia}'
      f_nacimiento = datetime.strptime(f_nacimiento_str, "%Y-%m-%d")
      edad = calculo_edad(f_nacimiento)
      print (f'Según su fecha de nacimiento indicada, {dia}-{mes}-{anyo}, usted tiene {edad} años.')
      break
    else :
      print('Los datos deben ser numéricos y seguir el ejemplo dado.')
  else :
    print('Los datos deben ser numéricos y seguir el ejemplo dado.')