# Primalidad numero divisibles por 1 y el mismo
from asyncio.proactor_events import _ProactorBasePipeTransport
def es_primo(numero):
    contador = 0
    for i in range(1,numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1        
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Digite un numero: "))
    if es_primo(numero):
        print("El numero es primo")
    else:
        print("El numero no es primo")
    #for i to range(100):
    #    pass



if __name__ == '__main__':
    run()

