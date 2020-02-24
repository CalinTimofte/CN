def ex1():
    u = 1
    exponent = 0
    while(1 + u != 1):
        u = u * (10 ** -1)
        exponent += 1
    return (u,exponent)

u, exponent = ex1()
print((10 ** (-exponent)) + 1)