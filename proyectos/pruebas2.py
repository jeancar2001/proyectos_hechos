def run(numero):
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

numero = 0
while numero < 500:
    numero +=1

    if run(numero):
        print(f' {numero}  es primo')
    else:
        print(f' {numero}  No es primo')