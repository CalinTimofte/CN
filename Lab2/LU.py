import copy

import numpy
import scipy.linalg as la


# 1 determinare matrici L si U
# done, to check
def descompunereLU(A, n):
    for p in range(n):
        # calculul elementelor liniei p din matricea U
        for i in range(p, n):
            sum = 0
            for k in range(p):
                sum += (A[p][k] * A[k][i])
            A[p][i] = A[p][i] - sum
        # calculul elementelor coloanei p din matricea L
        for i in range(p, n):
            if p == i:
                continue
            else:
                sum = 0
                for k in range(p):
                    sum += (A[i][k] * A[k][p])
                if A[p][p] != 0:
                    A[i][p] = (A[i][p] - sum) / A[p][p]


# 2 determinant A with L, U
# done, to check
def determinantALU(A, n):
    detA = 1
    for i in range(n):
        detA *= A[i][i]
    return detA


# 3 cautare solutie sistem de ecuatie
# undone, completat cu cazurile A[i][i], precizia calculelor epsilon
def calculare_solutieLU(A, n, b):
    y = []
    for i in range(n):
        sum = 0
        for j in range(i):
            sum = sum + A[i][j] * y[j]
        y.append((b[i] - sum))
    x = numpy.zeros(n)
    for i in reversed(range(n)):
        sum = 0
        for j in range(i-1,n):
            sum = sum + A[i][j] * x[j]
        x[i] = (y[i] - sum) / A[i][i]
    return x


# 4 calculul normei folosind A initiala, b initiala si solutia ecuatiei
# done, to check
def calcul_norma(A, n, b, x):
    # a init * x = y
    y = []
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += A[i][j] * x[j]
        y.append(sum)

    # y - b init = z
    for i in range(n):
        y[i] -= b[i]

    # ||z||
    sum = 0
    for i in range(n):
        sum += y[i] ** 2
    norma = sum ** (1 / 2)
    return norma


# 5 solutia sistemului si inversa matricii folosind lib
# done, don't think there is anything to check :)))
def done_with_libraries(A, n, b, xLU):
    xlib = numpy.linalg.solve(A, b)
    print("Solutia ecuatiei folosind libraria numpy: " + str(xlib) + "\n")
    Ainv = numpy.linalg.inv(A)
    print("A invers folosind libraria numpy: \n" + str(Ainv) + "\n")
    print("Verificare norma ||xLU - xlib||2: " + str(numpy.linalg.norm(xLU - xlib)) + "\n")
    print("Verificare cu norma ||xLU - A inv lib * b init||2: " + str(numpy.linalg.norm(xLU - numpy.dot(Ainv, b))) + "\n")


# 6 determinare inversul matricii
def inversa_matricii(A, n, Ainit):
    Ainv = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        e = [0 for j in range(n)]
        e[i] = 1
        xstar = calculare_solutieLU(A, n, e)
        for j in range(n):
            Ainv[i][j] = xstar[j]
    Alibinv = numpy.linalg.inv(Ainit)
    sumlist = []
    for i in range(n):
        sum = 0
        for j in range(n):
            if Ainv[i][j] - Alibinv[i][j] <0:
                sum += (Ainv[i][j] - Alibinv[i][j]) *(-1)
            else:
                sum += (Ainv[i][j] - Alibinv[i][j])
        sumlist.append(sum)
    C = max(sumlist)
    return C


def tema2(A, b, Ainit):
    n = len(A)
    binit = copy.deepcopy(b)
    print("A initial: " + str(A) + "\n")
    print("A dupa descompunere LU: " + str(descompunereLU(A, n)) + "\n")
    print("Determinant A: " + str(determinantALU(A, n)) + "\n")
    print("Solutia sistemului folosind LU: " + str(calculare_solutieLU(A,n,b)) + "\n")
    x = calculare_solutieLU(A,n,b)
    print("Norma calculata este: " + str(calcul_norma(Ainit, n, binit, x)) + "\n")
    done_with_libraries(Ainit, n, binit, x)
    print(inversa_matricii(A, n, Ainit))

A=[[2.5, 2, 2],
       [5, 6, 5],
       [5, 6, 6.5]]
b = [2,2,2]
Ainit = copy.deepcopy(A)
tema2(A, b, Ainit)
