# Calculo de Inversión.

capital_inicial = input("Ingrese el capital que desea invertir: ")
capital_inicial = float(capital_inicial)
interes_anual = input("Ingrese el interes anual en decimales: ")
interes_anual = float(interes_anual)
tiempo = input("Ingrese el numero de años que desea manter la inversión: ")
tiempo = float(tiempo)

capital_final = capital_inicial*(1+interes_anual)**tiempo
capital_final = round(capital_final)

print("El Capital Final sera el siguiente: ",capital_final)