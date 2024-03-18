'''
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''
def suma (n1,n2): #Pack de funciones de operación
  suma = n1 + n2
  return suma
def resta (n1,n2):
  resta = n1 - n2
  return resta
def multiplicacion (n1,n2):
  multiplicacion = n1 * n2
  return multiplicacion
def division (n1,n2):
  if n2 != 0 :
    division = n1 / n2
    return division
  else :
    return 'No se puede dividir entre 0'
flujo = True
while flujo :
  print ('Bienvenidos a la calculadora. Por favor, introduzca la opción (número) de la operacuón que quiera realizar:')
  print('1 - Sumar.')
  print('2 - Restar.')
  print('3 - Multiplicar.')
  print('4 - Dividir.')
  operacion = input ()
  print()
  if operacion in ['1','2','3','4']:
    if operacion == '1' : #Preguntamos la operación
      print ('¿Qué numeros desea sumar?')
    elif operacion == '2' :
      print ('¿Qué numeros desea restar?')
    elif operacion == '3' :
      print ('¿Qué numeros desea multiplicar?')
    elif operacion == '4' :
      print ('¿Qué numeros desea dividir?')
    n1 = input('Primer número: ') #Pedimos los números a operar
    n2 = input('Segundo número: ')
    def is_float(x) :
      try :
        float (x)
        return True
      except :
        return False
    if is_float(n1) and is_float(n2) :
      n1 = float(n1)
      n2 = float(n2)
      if operacion == '1' : #Operamos según la elección y sacamos el resultado
        resultado = suma(n1,n2)
        print (f'La suma de los números {n1} y {n2} es {resultado}.')
      if operacion == '2' :
        resultado = resta(n1,n2)
        print (f'La resta de los números {n1} y {n2} es {resultado}.')
      if operacion == '3' :
        resultado = multiplicacion(n1,n2)
        print (f'La multiplicación de los números {n1} y {n2} es {resultado}.')
      elif operacion == '4' :
        resultado = division(n1,n2)
        if n2 != 0 : #Si el segundo número es 0 el mensaje cambiaría
          print (f'La división de {n1} entre {n2} es {resultado}.')
        else :
          print(resultado)
      while flujo : #Creamos un bucle para preguntar si queremos volver a usar la calculadora
        volver = input ('¿Quiere volver a usar la calculadora? Responder: "Si" o "No": ')
        if volver.lower() =='si' :
          break
        elif volver.lower() == 'no' : #Con esto cerramos el flujo de todo el programa
          flujo = False
        else :
          print ('Por favor, elija una opción válida.')
          print()
    else :
      print('Debe introducir números para operar.')
  else :
    print ('Por favor, elija una opción válida.')
    print()