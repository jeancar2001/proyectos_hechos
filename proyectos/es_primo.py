def es_primo(numero):
    if numero == 1:
        return False
    else:
        contador = 0

        for i in range (1, numero+1):
            if i == 1 or i == numero:
                continue
            if numero % i == 0:
                contador +=1
    
        if contador == 0:
            return True
        else:
            return False


def run():
    while True:
        while True:
            numero = int(input("Escriba un numero del 1 al 10000:  "))
            if numero < 10001:
                break
            else:
                print("Por favor esciba un numero con el rango indicado...")
                continue
            
        if es_primo(numero):
            print("Es primo...")
        else:
            print("No es primo...")
        while True:    
            opcion = input("Desea seguir usando el programa[S/N]:  ")
            if opcion.upper() == "S":
                break
            elif opcion.upper() == "N":
                print ("Programa termiando correctamente...")
                exit()
            else:
                print("Por favor escoja una de las opciones mostradas...")


if __name__ == "__main__":
    run()