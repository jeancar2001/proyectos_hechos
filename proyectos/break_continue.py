def run ():
    numero_usuario = int(input('escriba un numero: '))

    for numero in range(1,numero_usuario+2):
        if numero % 2 != 0:
            continue
        print(numero)


if __name__ == '__main__' :
    run()