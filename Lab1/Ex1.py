import math

A = [[1,0,1,1,1,0,1,1], [1,0,1,1,1,0,1,1], [1,0,1,1,1,0,1,1], [1,0,1,1,1,0,1,1], [1,0,1,1,1,0,1,1], [1,0,1,1,1,0,1,1],
     [1,0,1,1,1,0,1,1], [1,0,1,1,1,0,1,1]]
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
    m = math.floor(math.log(n)) #dimensiunea matricilor mici
    p = math.ceil(n/m) #nr total de matrici

def slice_matrix_horizontally(B, m, p, n):
    return_matrixes = []
    for i in range(p):
        if i is not p - 1:
            return_matrixes.append([])
            for j in range(m):
                    # referinta!!
                    return_matrixes[i].append(B[j+(m*i)])
        else:
            return_matrixes.append([])
            for j in range(m*i, n):
                return_matrixes[i].append(B[j])
            if m*(i+1) != n:
                for j in (n, m*(i+1)):
                    return_matrixes[i].append([0 for x in range(n)])
    return return_matrixes


#
# x = ex1()[0];
# print((100*x) * x)
# print(100 * (x * x))
print(slice_matrix_horizontally(A, math.floor(math.log(len(A))), math.ceil(len(A)/(math.floor(math.log(len(A))))), len(A)))
