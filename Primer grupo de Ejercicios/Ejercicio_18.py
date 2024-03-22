'''
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''
# def contar_palabras (frase) : # Por si quieres saber las letras en vez de las palabras
#   contador = 0
#   caracteres = '1234567890. '
#   for palabra in frase :
#     contador += 1
#     for caracter in caracteres :
#       if palabra == caracter :
#         contador -= 1
#   return contador

def contar_palabras (frase) : # Contamos  las letras con el método .split() y len(), para saber la "longitud del split", excluyendo los puntos y las comas.
  palabras = len(frase.split())
  for caracter in frase.split () :
    if caracter == '.'  or caracter == ',':
      palabras -= 1
  return palabras

frase = input ('Por favor, introduzca una frase para contar la cantidad de palabras que contiene: ')
caracteres = contar_palabras(frase)
print(f'Su frase, "{frase}", contiene {caracteres} palabras.')