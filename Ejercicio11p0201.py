# Calculo de inetereses en una cuenta de ahorro.

capital = input("Por favor ingresa el capital con el que abriras la cuenta de ahorro:")
capital = float(capital)

interes1 = 1+4/100
interes2 = 4/100

A1 = round((capital*interes1),2)
A1B = round((capital*interes2),2)
A2 = round((A1*interes1),2)
A2B = round((A1*interes2),2)
A3 = round((A2*interes1),2)
A3B = round((A2*interes2),2)

print("El ahorro por interes del 4% acumulado en el primert año: ", 
      A1B, "y el Capital Final 1er. Año es: ", A1)
print("El ahorro por interes del 4% acumulado en el segundo año: ", 
      A2B, "y el Capital Final 1er. Año es: ", A2)
print("El ahorro por interes del 4% acumulado en el tercer año: ", 
      A3B, "y el Capital Final 1er. Año es: ", A3)
