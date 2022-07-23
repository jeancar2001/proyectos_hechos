
def conversor (valor_dolares):
    resultado = str(round(valor_pesos/valor_dolares, 2))
    print ("Tiene " + resultado + " dolares " )


valor_pesos = float(input("Ingrese cuantos pesos tiene:  "))

opcion = input ("""Ingrese que tipo de pesos posee
                            [1] Pesos Argentinos
                            [2] Pesos Mexicanos
                            [3] Pesos Colombianos
                                """)


if opcion == "1":
    conversor (117.24)
elif opcion == "2":
    conversor(20.25)
elif opcion == "3":
    conversor(4108.11)
else:
    print("Por Favor escoja una opcion correcta")
    exit()

print("El Programa se ejecuto correctamente...")