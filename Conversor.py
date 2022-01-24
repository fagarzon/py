# Observación probando


def conversor(tipo_peso, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_peso +  " tienes?:  ")
    pesos = float(pesos)
    valor_dolar = valor_dolar
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")    

menu = """
Bienvenido al conversor

1. Pesos colombianos
2. Pesos argentinos
3. Pesos Mexicanos

Escoger una Opción
"""
opcion = input(menu)

if opcion == "1":
    conversor("Colombianos" , 3875)
elif opcion == "2":
    conversor("Argentinos" , 65)
elif opcion == "3":
    conversor("Mexicanos" , 24)
else:
    print("opcion incorrecta")



