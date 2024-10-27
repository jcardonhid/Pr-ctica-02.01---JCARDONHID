# Calculo IMC

peso = input("Por favor introduce tu peso en kilogramos: ")
peso = float(peso)
estatura = input("Por favor introduce tu estatura en metros: ")
estatura = float(estatura)
imc = peso/(estatura)**2
imc = round(imc,2)
print("Tu índice de masa corporal es: ", imc)