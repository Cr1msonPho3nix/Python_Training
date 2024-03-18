'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''
semana = {
  1: 'Lunes',
  2: 'Martes',
  3: 'Miércoles',
  4: 'Jueves',
  5: 'Viernes',
  6: 'Sábado',
  7: 'Domingo'
}
while True :
  dia_semana = input ('Introduzca un número correspondiente al día de la semana, comenzando desde el 1 (Lunes) hasta el 7 (Domingo): ')
  if dia_semana.isdigit() :
    dia_semana = int(dia_semana)
    if 1 <= dia_semana <= 7 :
      print(f'El día de la semana que ha elegido, {dia_semana}, corresponde al día {semana[dia_semana]}')
      break
    else :
      print('Por favor, introduzca un número del 1 al 7.')
      print()
  else :
    print('Por favor, introduzca un número del 1 al 7.')
    print()