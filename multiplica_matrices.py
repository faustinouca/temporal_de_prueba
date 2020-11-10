p = int(input('Dime el número de filas de la matriz A: '))
q = int(input('Dime el número de columnas de la matriz A y de filas de B: '))
r = int(input('Dime el número de columnas de B: '))

# Creamos dos matrices nulas
A = []
for i in range(p):
    A.append([0] * q)

B = []
for i in range(q):
    B.append([0] * r)

# ... y leemos sus contenidos del teclado

print('Lectura de la Matriz A ')
for i in range(q):
    for j in range(r):
        B[i][j] = int(input(' Componente {0} {1}: '.format(i, j)))

# Creamos una matriz nula más para el resultado.

C = []
for i in range(p):
    C.append([0] * r)

# Y efectuamos el cálculo del producto
for i in range(p):
    for j in range(r):
        for k in range(q):
            C[i][j] += A[i][k] * B[k][j]
