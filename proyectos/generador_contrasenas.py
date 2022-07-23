import random

def contrasena_aleatoria():
    caracteres = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

    contrasena = []
    for i in range(15):
        caracter_aleatorio = random.choice(caracteres)
        contrasena.append(caracter_aleatorio)
    
    contrasena = "\n".join(contrasena)
    return contrasena

def run():
    contrasena = contrasena_aleatoria()
    print("Su contraseña es: " + contrasena)




if __name__ == "__main__":
    run()