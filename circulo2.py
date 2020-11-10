from math import pi

radio = float(input('Dame el radio de un circulo: '))
opcion = ''
while opcion != 'd':
    print('Escoge una opcion: ')
    print('a) Calcular el diámetro.')
    print('b) Calcular el perímetro.')
    print('c) Calcular el área.')
    print('d) Finalizar.')
    opcion = input('Teclea a b c o d y pulsa el retorno de carro: ')
    if opcion == 'a':
        diametro = 2 * area
        print('El diámetro es', diametro)
    elif opcion == 'b':
        perimetro = 2 * pi * radio
        print('El perímetro es ', perimetro)
    elif opcion == 'c':
        area = pi * radio ** 2
        print('El área es', area)
    elif opcion != 'd':
        print('Solo hay cuatro opciones: a b c o d. Tu has tecleado', opcion)

print('Gracias por usar el programa')
    
