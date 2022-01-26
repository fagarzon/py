def run():
    numero = [1, 3, 6, 9, 45, 90]
    objetos = ['hola', 3, True]
    #agregar objetos a la lista
    objetos.append(False)
    #quitar objetos a la lista
    objetos.pop(1)
    #reorrer objetos
    for elemento in objetos:
        print(elemento)    
    #print(numero)
    print(objetos)
    print(objetos[::-1])


def run_tuplas():
    numeros = [1,2,3,4,5]    
    print(numeros)
    numero2 =[6,7,8,9,0]
    lista_final = numeros + numero2
    print(lista_final)
    print(numeros * 5)
    #listas son dinamicas - py necesita mas memoria por eso usa tuplas
    #tupla tipo de objeto estatico - iteraciones recorremos tupla ejecucion mas rapida
    #tuplas inmutables - no puede cambiar
    tupla = (1,2,3,4,5)
    print(tupla)


if __name__ == '__main__':
    #run()
    run_tuplas()

