'''
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.
'''
# Función completa
def mayor_edad () :
  while True :  # Bucle por si el usuario no introduce un número válido.
    edad = input('Por favor, introduzca su edad para saber si es mayor de edad: ')
    if edad.isdigit():
      edad = int(edad)
      if edad >=18 :  # Si tiene más o igual a 18.
        print()
        print(f'Usted, con {edad} años, es mayor de edad.')
        break
      else :  # Si tiene menos de 18.
        print()
        print(f'Usted, con {edad} años, NO es mayor de edad.')
        break
    else :  # Si no se introducen números.
      print()
      print('Introduzca un número válido.')
mayor_edad()