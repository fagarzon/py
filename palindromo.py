# Rebanadas - slide
#nombre = input('Escriba un Nombre')
#nombre_slide = nombre[0:3]
#print(nombre)
#print(nombre_slide)
#print(nombre[3:])
#print(nombre[1:5])
#print(nombre[1:10:2])
#print(nombre[::-1])

#Ejempo Luz Azul se lee igual 
from pickle import FALSE, TRUE


def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:        
        return False


def run():
    palabra = input('Escriba un Palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('la palabra Es palindromo')
    else:
        print('la palabra NO Es palindromo')


#punto de entrda de una programa python
if __name__ == '__main__':
    run() 



