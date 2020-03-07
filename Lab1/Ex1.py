import math

import numpy

A = [[1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1],
     [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1],
     [1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1]]
B = [[0, 0, 0, 1], [1, 1, 1, 1]]


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


def num(vectorA):
    numerar = 0b0
    for i in reversed(vectorA):
        numerar = numerar * 10 + i
    return numerar


def slice_matrix_vertically(A, m, p, n):
    return_matrixes = []
    return_matrixes_original = []
    transposeA = numpy.transpose(A)
    for i in range(p):
        if i is not p - 1:
            return_matrixes.append([])
            for j in range(m):
                # referinta!!
                return_matrixes[i].append(transposeA[j + (m * i)])
        else:
            return_matrixes.append([])
            for j in range(m * i, n):
                return_matrixes[i].append(transposeA[j])
            if m * (i + 1) != n:
                for j in (n, m * (i + 1)):
                    return_matrixes[i].append([0 for x in range(n)])
    for matrix in return_matrixes:
        transposeMatrix = numpy.transpose(matrix)
        return_matrixes_original.append(transposeMatrix)
    return return_matrixes_original


def slice_matrix_horizontally(B, m, p, n):
    return_matrixes = []
    for i in range(p):
        if i is not p - 1:
            return_matrixes.append([])
            for j in range(m):
                # referinta!!
                return_matrixes[i].append(B[j + (m * i)])
        else:
            return_matrixes.append([])
            for j in range(m * i, n):
                return_matrixes[i].append(B[j])
            if m * (i + 1) != n:
                for j in (n, m * (i + 1)):
                    return_matrixes[i].append([0 for x in range(n)])
    return return_matrixes


def ex3(matrix_A, matrix_B):
    n = len(matrix_A)
    m = math.floor(math.log(n))  # dimensiunea matricilor mici
    p = math.ceil(n / m)  # nr total de matrici
    matrix_C = []
    # 1
    anyA = (slice_matrix_vertically(matrix_A, m, p, n))

    # 2
    anyB = (slice_matrix_horizontally(matrix_B, m, p, n))

    # 3
    for i in range(1, p):
        sum_linii_B = [[0 for contor in range(1, n)]]
        for j in range(1, 2 ** m - 1):
            k = int(math.log(j, 2))
            print(k)
            # trebuie facuta suma pe biti pentru vectori
            sum_linii_B.append(sum_linii_B[j - (2 ** k)] & anyB[i][k + 1])
            print(sum_linii_B)
    for i in range(1, p):
        for r in range(1, n):
            matrix_C[i].append(sum_linii_B[num(anyA[i][r])])
    print(matrix_C)
    # 4


#
# x = ex1()[0];
# print((100*x) * x)
# print(100 * (x * x))
# print(slice_matrix_horizontally(A, math.floor(math.log(len(A))), math.ceil(len(A) / (math.floor(math.log(len(A))))),
#                                len(A)))

# print(slice_matrix_vertically(A, math.floor(math.log(len(A))), math.ceil(len(A) / (math.floor(math.log(len(A))))),
#                              len(A)))

ex3(A, A)