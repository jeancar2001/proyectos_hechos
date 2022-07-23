
dolar_euro = 0.95

valor_dinero = float(input("Escriba el valor de dinero que tenga: "))

opcion = input("Escoja una opcion a convertir  \n"
                                "[A] Dolar a Euro \n" 
                                "[B] Euro a Dolar \n"
                                "Opcion:  " )
                            
valor_convertido = None

if opcion == "A":
    valor_convertido = round(valor_dinero*dolar_euro , 2)
    valor_convertido = str(valor_convertido)
    print("El valor ingresado equivale a " + valor_convertido + " Euros")

elif opcion == "B":
    valor_convertido = round(valor_dinero/dolar_euro , 2)
    valor_convertido = str(valor_convertido)
    print("El valor ingresado equivale a " + valor_convertido + " Dolares")
else:
    print ("Por Favor escoja una de las opciones mostradas...")
    exit()

print("El Programa ha finalizado correctamente...")
