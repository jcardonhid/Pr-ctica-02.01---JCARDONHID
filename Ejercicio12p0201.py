#Calculo de descuento en barras de pan.

nbarras = input("Ingresa el número de barras, que no son del día, y que se vendieron el día de hoy: ")
nbarras = int(nbarras)
precio = nbarras*3.49
precio = round(precio,2)
descuento = precio*0.6
descuento = round(descuento,2)
ganancia = precio-descuento
ganancia = round(ganancia,2)

print(nbarras, "barras de pan a 3.49 euros c/u da un precio habitual de:", precio, "euros")
print("Descuento por la venta de:", nbarras, "barras de pan del día anterior (60%):", descuento, "euros")
print("Ganancia por la venta de:", nbarras, "barras de pan del día anterior:", ganancia, "euros")
