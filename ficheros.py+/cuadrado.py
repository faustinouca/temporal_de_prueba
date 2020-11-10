import math

def cuadrado(x):
    return x ** 2


print(cuadrado(3))


def raiz_cubica(x):
    return x ** (1/3)


print(raiz_cubica(9))

print(math.pi)


def es_repeticion(x, y):
    n = len(y) % len(x)
    if n > 0:
        return("False")

    print(len(y))
    print(len(x))
    n = int(len(y) / len(x))
    print(" ")
    print(" n = {0}".format(n))
    print(" ")
    s = 0
    z = len(x)
    for i in range(n):
        print(" i = {0} ".format(i))
        print("y[s:len(x)] ".format(y[s:len(x)]))
        print(" ")
        if y[s:z] != x:
            return("False")
        else:
            s += len(x)
            z += len(x)
            print(" s = {0}".format(s))

    return("True")


print(es_repeticion("ab", "ababavabxb"))
