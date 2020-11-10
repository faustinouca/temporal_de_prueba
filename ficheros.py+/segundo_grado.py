from math import sqrt
print('Programa para la resulución de la ecuación de segundo grado ax^2+bx+c=0')
a = float(input('Valor de a:'))
b = float(input('Valor de b:'))
c = float(input('Valor de c:'))

if a != 0:
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    print('Soluciones : x1 ? {0:.3f}) y x2={1:.3f}' .format(x1, x2))

if a == 0:
    print('No es una ecuación de segundo grado')
