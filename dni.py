salir = False
letra_dni = 'TRWAGMYFPDXBNJZSQVHLCKE'
while not salir:
    print('Programa para la resulución de la letra correspondiente al DNI')
    dni = input('Introduzca el DNI sin letra: ')
    if len(str(dni)) != 8:
        print('Introduzca un número válido, sin blancos')
    else:
        suma_digitos = 0
        for j in range(0, 8):
            suma_digitos += int(dni[j])

    print('\nLa letra correspondiente al DNI :', letra_dni[suma_digitos % 23])
    print(suma_digitos)
    print(suma_digitos % 23)
