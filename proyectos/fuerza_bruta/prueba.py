# def division():
#     number = int(input("escriba un numero"))
#     number2 = int(input("escriba un numero"))
#     return number/number2

# def division2():
#     number = int(input("ejecutando division 2.escriba un numero 1"))
#     number2 = int(input("ejecutando division 2.escriba un numero 2"))
#     return number/number2


# if __name__ == "__main__":
#     try:
#         print(division())
#     except:
#         print("ocurrio un error")
#         print(division2())
#     else:
#         print("sin errores")
import random

def number_1():
    bin = ""
    while True:
        n_c = bin
        for i in range(10):
            n_c += str(random.randint(0,9))
        a = 0
        for i in range(10):
            if i  % 2 == 0:
                if int(n_c[i])*2 >=10:
                    j = str(int(n_c[i])*2)
                    j = int(j[0])+int(j[1])
                    a += j
                else:
                    a += int(n_c[i])*2
            else:
                a += int(n_c[i])
        if a % 10 == 0:
            return str(n_c)
        else:
            continue


print(number_1())