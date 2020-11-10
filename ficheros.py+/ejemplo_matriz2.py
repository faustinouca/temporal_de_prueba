M = []
for i in range(4):
    M.append([0]*4)
print(M)
# range da un número que empieza por 0 y acaba en el número final - 1
for i in range(0, 4):
    M[i][i] = 1

print(M)
