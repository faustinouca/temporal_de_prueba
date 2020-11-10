# Pedimos la dimensión de la matriz
m = int(input('Introduzca el número de filas: '))
n = int(input('Dime el número de columnas: '))

# Creamos una matriz nula
M = []
for i in range(m):
    M.append([0] * n)

# ...y leemos su contenido de teclado
for i in range(m):
    for j in range(n):
        M[i][j] = int(input('Introduzca el componente ({0},{1}): '.format(i, j)))

for i in range(0, m):
    print(M[i])
