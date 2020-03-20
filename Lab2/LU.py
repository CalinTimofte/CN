import copy

import numpy
import scipy.linalg as la

eps = 0.0000001


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
                if abs(A[p][p]) > eps:
                    A[i][p] = (A[i][p] - sum) / A[p][p]
                else:
                    print("Nu se poate face impartirea \n")
                    break


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
        for j in range(i, n):
            sum = sum + A[i][j] * x[j]
        if abs(A[i][i]) > eps:
            x[i] = (y[i] - sum) / A[i][i]
        else:
            print("Nu se poate face impartirea")
            break
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
    print("Verificare norma ||xLU - xlib||2: " + str(numpy.linalg.norm(xLU - xlib,2)) + "\n")
    print(
        "Verificare cu norma ||xLU - A inv lib * b init||2: " + str(numpy.linalg.norm(xLU - numpy.dot(Ainv, b),2)) + "\n")


# 6 determinare inversul matricii
def inversa_matricii(A, n, Ainit):
    Ainv = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        e = [0 for j in range(n)]
        e[i] = 1
        xstar = calculare_solutieLU(A, n, e)
        for j in range(n):
            Ainv[j][i] = xstar[j]
    print("Inversa calculata este: ")
    for i in range(n):
        print(Ainv[i])
    print("\n")
    Alibinv = numpy.linalg.inv(Ainit)
    print("Inversa de la numpy: \n" + str(Alibinv) + "\n")
    C = numpy.linalg.norm(abs(Ainv - Alibinv),1)
    return C


def tema2(A, b, Ainit):
    n = len(A)
    binit = copy.deepcopy(b)
    print("A initial: " + str(A) + "\n")
    print("A dupa descompunere LU: " + str(descompunereLU(A, n)) + "\n")
    print("Determinant A: " + str(determinantALU(A, n)) + "\n")
    print("Solutia sistemului folosind LU: " + str(calculare_solutieLU(A, n, b)) + "\n")
    x = calculare_solutieLU(A, n, b)
    print("Norma calculata este: " + str(calcul_norma(Ainit, n, binit, x)) + "\n")
    done_with_libraries(Ainit, n, binit, x)
    print("Norma de ordin 1 ||AinvLU - Alibinv||1: " + str(inversa_matricii(A, n, Ainit)) + "\n")


A = [[2.5, 2, 2],
     [5, 6, 5],
     [5, 6, 6.5]]
b = [2, 2, 2]
Ainit = copy.deepcopy(A)
tema2(A, b, Ainit)
