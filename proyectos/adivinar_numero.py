import random

def run():
    while True:
        numero_aleatorio = random.randint (1,1000)
        print (numero_aleatorio)
        numero_usuario = int(input("Escoja un numero del 1 al 1000:  "))

        while numero_usuario != numero_aleatorio:
            if numero_usuario < numero_aleatorio:
                print("Escoja un numero mas grande...")
            else:
                print("Escoja un numero mas grande...")
            numero_usuario = int(input("Escoja otro numero...:  "))
        
        print("Ganaste es el numero correcto...")
        while True:
            opcion = input("Desea seguir jugando?[S/N]:  ")
            if opcion.upper() == "S":
                print('A seguir jugando entonces....')
                break
            elif opcion.upper() == "N":
                print ("Juego Cerrado... ")
                print("Programa terminado correctamente")
                exit()
            else:
                print ("Por favor escoja una opcion correcta...")

if __name__ == "__main__":
    run()