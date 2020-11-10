marcas_motos = ['ducati', 'yamaha', 'honda', 'suzuki', 'bmw']
print(marcas_motos)
marcas_motos.append('indian')
print(marcas_motos)
marcas_motos.insert(2, 'bultaco')
print(marcas_motos)
del marcas_motos[0]
print(marcas_motos)
ultima_marca = marcas_motos.pop()
print(ultima_marca)
print(marcas_motos)
print('La lista de motos tiene {0} elementos '.format(len(marcas_motos)))
marcas_motos.sort()
print(marcas_motos)
marcas_motos.sort(reverse=True)
print(marcas_motos)
print(' ')
print(' ')
print(sorted(marcas_motos))
marcas_motos.reverse()
print(marcas_motos)
print(' ')
print(' ')
requested_toppings = ['setas', 'pimientos', 'queso']
for requested in requested_toppings:
    if requested == 'pimientos':
        print('Lo siento no tenemos pimientos')
    else:
        print('Añadiendo ' + requested + '.')
print('Pizza terminada')
print(' ')
print(' ')
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Valor: ' + value)
print(' ')
print(' ')
lenguajes_favoritos = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}

print('Los siguientes lenguajes han sido mencionados ')
for lenguaje in lenguajes_favoritos.values():
    print(lenguaje.title())
