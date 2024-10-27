# Calculo de Peso de un Pedido.

payasos = input("Por favor ingrese el numero de payasos que se incluyen en este pedido: ")
payasos = int(payasos)
munecas = input("Por favor ingrese el numero de muñecas que se encluyen en este pedido: ")
munecas = int(munecas)

peso_payaso = 112
peso_muneca = 75

peso_paquete = (payasos*peso_payaso)+(munecas*peso_muneca)

print("El paquete a enviar tiene un peso de: ", peso_paquete, "gramos")