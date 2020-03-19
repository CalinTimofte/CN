from builtins import range
import numpy
#determinare matrici L si U
import scipy.linalg as la


def LU(A,n):
    #calculul elementelor liniei p din matricea U
    U = [[0 for x in range(n)]
         for y in range(n)]
    L=[[0 for x in range(n)]
       for y in range(n)]
    for p in range(n):
        for i in range(p,n):
            sum=0
            for k in range(p):
                sum+= (L[p][k] * U[k][i])
            U[p][i]= A[p][i] - sum
        for i in range(p,n):
            if p==i:
                L[i][i]=1
            else:
                sum=0
                for k in range(p):
                    sum+= (L[i][k]*U[k][p])
                if U[p][p]!=0:
                    L[i][p] = (A[i][p] - sum) / U[p][p]
    print(la.lu(A))

#def ex1(n,epsilon, A, b):
#    Ainit = A.copy()
#    for i in range(n):


LU([[2, -1, -2],
       [-4, 6, 3],
       [-4, -2, 8]],3)

