
# Salario por horas trabajadas.

horas=0
coste=0
salario=0

horas = input('¿Cuantas horas has trabajado?')
coste = input('¿Cual es el salario por hora?')

horas = float(horas)
coste = float(coste)
salario = horas*coste

print('Te corresponde un salario de', salario, 'euros.')