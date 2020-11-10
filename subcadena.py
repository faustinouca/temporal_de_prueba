cadena = input('Dame una cadena: ')
i = int(input('Dame un número: '))
j = int(input('Dame otro número: '))

subcadena = ''

for k in range(i, j):
    subcadena += cadena[k]

print('La subcadena entre {0} y {1} es {2}.'.format(i, j, subcadena))
