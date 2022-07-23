

def run():
    LIMITE = 1000
    contador = 0
    elevado_2 = 2**contador

    while elevado_2 < LIMITE:
        print ("2 elevado a " + str(contador)+ " es igua a " + str(elevado_2))

        contador +=1
        elevado_2 = 2**contador

if __name__ == "__main__":
    run()