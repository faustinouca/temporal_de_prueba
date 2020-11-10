lista = [2, 26, 4, 3, 1]

for i in range(1, len(lista)):
    # i es un contador que va a repetir el bucle tantas veces como la
    # longitud de la lista menos 1
    print('Pasada ', i)
    for j in range(0, len(lista)-i):
        # Llegamos siempre hasta el elemento anterior al último
        print('  Comparación de {0} y {1}'.format(lista[j], lista[j+1]))
        if lista[j] > lista[j+1]:
            elemento = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = elemento
            print('Se intercambian')
        print(' Estado actual de la lista', lista)
        print(' ')
print(' ')
print(' Resultado final', lista)
