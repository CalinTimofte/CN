def ex1():
    u = 1
    exponent = 0
    while 1 + u != 1:
        u = u * (10 ** -1)
        exponent += 1
    return u, exponent


def ex2():
    xSuma = 1.0
    xProdus = 100
    y = ex1()[0]
    z = ex1()[0]
    print("Suma e " + str((xSuma + y) + z == xSuma + (y + z)))
    print("Produsul e " + str((xProdus * y) * z == xProdus * (y * z)))


def ex3():
    pass


print(ex1())
ex2()
