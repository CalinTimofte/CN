import numpy
# determinare matrici L si U
import scipy.linalg as la


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
    print(A)


def determinantALU(A, n):
    detA = 1
    for i in range(n):
        detA *= A[i][i]
    print(detA)


# undone, completat cu cazurile A[i][i], precizia calculelor epsilon
def calculare_solutieLU(A, n, b):
    y = []
    for i in range(n):
        sum = 0
        for j in range(i):
            sum = sum + A[i][j] * y[j]
        y.append((b[i] - sum) / A[i][i])
    x = numpy.zeros(n)
    for i in reversed(range(n)):
        sum = 0
        for j in range(i + 1, n):
            sum = sum + A[i][j] * x[j]
        x[i] = (y[i] - sum) / A[i][i]
    return x


#to do
def calcul_norma(A,n,b,x):
    # a init * x = y
    # y - b init = z
    sum = 0
    for i in range(n):
        sum += z[i]**2
    norma = sum ** 1/2


#to do
def inversa_matricii:

def tema2(A, n, b):
    Ainit = A.copy()
    binit = b.copy()
    descompunereLU(A, n)
    determinantALU(A, n)
    x=calculare_solutieLU(A,n,b)
    calculare_solutieLU(Ainit, n, binit, x)


tema2([[2.5, 2, 2],
       [5, 6, 5],
       [5, 6, 6.5]], 3, [2, 2, 2])
