car = input('Dame un caracter: ')

if 'a' <= car.lower() <= 'z' or car == '-':
    print('Este carácter es válido en un identificador en Python')
else:
    if not (car < '0' or '9' < car):
        print('Un dígito es válido en un identificador en Python3. ', end='')
        print('siempre que no sea el primer carácter')
    else:
        print('Caracter no valido para un identificador phyton')
        
