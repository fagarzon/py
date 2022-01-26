
def run():
    #estructura de llaves y valores
    diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    print(diccionario)
    print(diccionario['llave2'])

    poblacion = {
        'colombia': 507584,
        'argentina': 503837584,
        'peru': 353837584
    }
    for pais in poblacion.keys():
        print(pais)
    for pais in poblacion.values():
        print(pais)
    for pais,poblacion in poblacion.items():
        print(pais +' Tiene ' + str(poblacion) + ' Habitantes.')

#entry poin
if __name__ == '__main__':
    run()