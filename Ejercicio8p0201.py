# Cálculo del cociente y el resto de una división.

n = input("Introduce un número entero como dividendo: ")
n = int(n)
m = input("Introduce un número entero como divisor: ")
m = int(m)

c = n/m
if c > 1:
    c = int(c)
else:
    c = float(c)

r = n%m
r = int(r)

print(n, "entre", m, "da un cociente de", c, "y un resto de", r)