
numero = float(input('Dame un número: '))

for n in range(2, 101):
    print('La raíz {0}-enesima de {1} es {2}'.format(n, numero, numero**(1/n)))
