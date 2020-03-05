import math

A = [[0,1,0,1],[1,0,0,1]]
B = [[0,0,0,1],[1,1,1,1]]

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


def ex3(matrix_A, matrix_B):
    n = len(matrix_A)
    m = math.floor(math.log(n)) #nr total de (linii sau coloane)/matrice
    p = math.ceil(n/m) #nr total de matrici

def slice_matrix_horizontally(B, m, p, n):
    return_matrixes = []
    for i in range(p):
        if i is not p - 1:
            for j in range(m):
                    # referinta!!
                    return_matrixes[i][j] = B[j+i]
        else:
            for j in range(m)


#
# x = ex1()[0];
# print((100*x) * x)
# print(100 * (x * x))
ex3(A,B)
