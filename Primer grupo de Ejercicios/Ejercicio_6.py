'''
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def palindromo (palabra) :
  palabra_inversa =''
  for letra in palabra[::-1] : #Crea palabra inversa
    palabra_inversa += letra
  if palabra == palabra_inversa: #Verifica si la palabra introducida en la misma que la inversa
    print (palabra_inversa)
    return True
  else :
    print (palabra_inversa)
    return False

while True:
  palabra = input('Por favor, introduzca una palabra para saber si es palíndroma: ')
  if not palabra.isdigit() : #Si la palabra NO tiene números
    if palindromo(palabra) :
      print(f'La palabra {palabra} es palíndroma.')
      break
    else :
      print(f'La palabra {palabra} NO es palíndroma.')
      break
  else : #Si la palabra tiene números vuelve al principio
    print ('Por favor, introduzca sólo letras.')