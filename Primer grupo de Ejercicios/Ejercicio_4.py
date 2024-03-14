'''
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''
def contar_vocales () :
  while True:
    palabra = input('Inserte la palabra a la que se le contarán las vocales: ')
    if palabra.isalpha() :
      vocales = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
      contador = 0
      for letra in palabra :
        if letra in vocales :
          contador += 1
      print(f'En su palabra, {palabra}, se han detectado {contador} vocales.')
      break
    else :
      print('Los números o símbolos no están permitidos.')
contar_vocales()