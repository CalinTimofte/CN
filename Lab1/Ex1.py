import math

import numpy

A = [[1, 0, 1, 1, 1, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 1, 0, 0],
     [1, 0, 1, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 1]]

B = [[1, 0, 1, 0, 1, 0, 1, 0],
     [0, 1, 0, 1, 0, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 1, 1, 1, 0],
     [1, 0, 0, 1, 1, 0, 1, 1],
     [1, 1, 0, 1, 1, 1, 1, 1],
     [1, 0, 1, 1, 1, 0, 0, 0]]


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


def num_int(vector):
    bin_num = num(vector)
    return int(str(bin_num), 2)


def byte_sum_list(list_1, list_2):
    return_list = []
    for i, j in zip(list_1, list_2):
        return_list.append(i | j)
    return return_list


def matrix_sum(A, B):
    return_matrix = []
    current_line = []
    for i in range(len(A)):
        current_line.clear()
        for j in range(len(A[i])):
            current_line.append(A[i][j] | B[i][j])
        return_matrix.append(current_line.copy())
    return return_matrix


# Functie pentru impartirea pe coloana
def slice_matrix_vertically(A, m, p, n):
    return_matrixes = []
    return_matrixes_original = []
    transposeA = numpy.transpose(A)
    for i in range(p):
        if i is not p - 1:
            return_matrixes.append([])
            for j in range(m):
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


# Functie pentru impartirea pe linie
def slice_matrix_horizontally(B, m, p, n):
    return_matrixes = []
    for i in range(p):
        if i is not p - 1:
            return_matrixes.append([])
            for j in range(m):
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
    C_i_matrix_list = []
    sum_linii_B = []
    
    # 1
    A_i_matrix_list = (slice_matrix_vertically(matrix_A, m, p, n))

    # 2
    B_i_matrix_list = (slice_matrix_horizontally(matrix_B, m, p, n))

    # 3
    for i in range(p):
        sum_linii_B.clear()
        sum_linii_B.append([0 for contor in range(n)])
        for j in range(1, (2 ** m)):
            k = int(math.log(j, 2))
            sum_linii_B.append(byte_sum_list(sum_linii_B[j - (2 ** k)], B_i_matrix_list[i][k]))
        C_i_matrix_list.append([])
        for r in range(n):
            C_i_matrix_list[i].append(sum_linii_B[num_int(A_i_matrix_list[i][r])].copy())

    # 4
    C = C_i_matrix_list[0]
    for i in range(
            1, len(C_i_matrix_list)):
        C = matrix_sum(C, C_i_matrix_list[i])
    return C


# x = ex1()[0];
# print((100*x) * x)
# print(100 * (x * x))

print(ex3(A, B))
