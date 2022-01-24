#contador = 1
#print ('2 Elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))
#contador = 2
#print ('2 Elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# While
def run_while():
    contador = 0
    LIMITE = 1000
    potencia_2 = 0
    while potencia_2 < LIMITE:
        print ('2 Elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

def run_for():
    #contador = 1
    #while contador < 100:
    #    print(contador)
    #    #contador = contador+ 1
    #    contador += 1
   for contador in range(1,101):
       print(contador)

if __name__ == '__main__':
    #run_while()
    run_for()


