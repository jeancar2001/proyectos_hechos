
def run ():
      resultados = []
      combinaciones = []
      resultadoscompletos = []

      a = input("Escriba los resultados: ")
      a = a.replace(" ","")

      b = input("Escriba las combinaciones: ")
      b = b.replace(" ","")
      c = ""
      d = 0
      for i in b:
            c += i
            if d == 27:
                  combinaciones.append(c)
                  c = ""
                  d = 0
                  continue
            d += 1

      for i in a:
            c += i
            if d == 15:
                  resultados.append(c)
                  c = ""
                  d = 0
                  continue
            d += 1
      
      for i in resultados:
            for j in combinaciones:
                  if i == j[0:16]:
                        resultadoscompletos.append(j)
                        break
      

      resultadoscompletos = "\n".join(resultadoscompletos)
      print(resultadoscompletos)


            
            
      

      


if __name__ == "__main__":
      run()