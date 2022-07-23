def run(): 
        numero_usuario = int(input("""Bienvenido al creador de tablas de multiplicar que tabla desea:  """))
        for numero in range (1,12+1):
            resultado = numero_usuario * numero
            print(f'{numero_usuario}' + 'x' + f'{numero}' +  '=' + f'{resultado}')
        run2()
        


def run2():
     while True: 
        opcion = input('Desea seguir usando el programa [S/N] : ')
        opcion = opcion.lower()

        if opcion == 's':
            run()
        elif opcion == 'n':
            print ('Entendido el programa se cerrara...')
            print('Programa terminado correctamente...')
            exit()
        else:
            print('Elija una opcion correcta por favor...')


if __name__ == '__main__':
    run()