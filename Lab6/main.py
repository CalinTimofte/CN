import numpy as np
import random
import math

epsilon = epsilon = 10 ** -9


def generate_numbers(x0, xn, f):
    x_values = []
    y_values = []
    # how_many_numbers = random.randint(1, int(xn-x0))
    how_many_numbers = 349
    x_values.append(x0)
    for i in range(how_many_numbers):
        new_number = random.uniform(x_values[i] + epsilon, xn - 1)
        x_values.append(new_number)
    x_values.append(xn)
    for i in x_values:
        y_values.append(f(i))
    return (x_values, y_values)


def interpolare_prin_metoda_celor_mai_mici_patrate(x_vector, y_vector):
    # m este egal cu lungimea x_vector ptc e nevoie sa fie matrice patratica sa mearga solve
    B = [[i ** j for j in range(len(x_vector))] for i in x_vector]
    f = [[i] for i in y_vector]
    B = np.array(B, dtype=float)
    f = np.array(f, dtype=float)
    a = np.linalg.solve(B, f)
    return a


def Horner(x, polynom_coefficients):
    polynom_coefficients = [x[0] for x in polynom_coefficients]
    for index, i in enumerate(polynom_coefficients):
        if index == 0:
            d = i
        else:
            d = i + d * x
    return d


def interpolare_trigonometrica(x_vector, y_vector):
    B = [[math.sin(i * j) if i % 2 == 1 else math.cos(i * j) for j in range(len(x_vector))] for i in x_vector]
    for i in range(len(B)):
        B[i][0] = 1
    f = [[i] for i in y_vector]
    B = np.array(B, dtype=float)
    f = np.array(f, dtype=float)
    a = np.linalg.solve(B, f)
    return a


def solutie_cu_interpolare_geometrica(a, x):
    for index, i in enumerate(a):
        i = i[0]
        if index == 0:
            solution = i
        elif index % 2 == 0:
            solution += i * math.sin(x * index)
        else:
            solution += i * math.cos(x * index)
    return solution


x1 = 0
y1 = 5


def func1(x):
    return x ** 4 + 12 * x ** 3 + 30 * x ** 2 + 12


x2 = 0
y2 = 31 * math.pi / 16


def func2(x):
    return math.sin(x) - math.cos(x)


x3 = 0
y3 = 31 * math.pi / 16


def func3(x):
    return math.sin(2 * x) + math.sin(x) + math.cos(3 * x)


x4 = 0
y4 = 63 * math.pi / 32


def func4(x):
    return math.sin(x) ** 2 - math.cos(x) ** 2


def test1(x, y, func, test_num):
    x, y = generate_numbers(x, y, func)
    polynom_coefficients = interpolare_prin_metoda_celor_mai_mici_patrate(x, y)
    # print(x)
    # print(y)
    # print(polynom_coefficients)
    rezultat1 = func(test_num)
    rezultat2 = Horner(test_num, polynom_coefficients)
    print(rezultat1)
    print(rezultat2)
    # print(abs(rezultat2 - rezultat1))


def test2(x, y, func, test_num):
    x, y = generate_numbers(x, y, func)
    coeficients = interpolare_trigonometrica(x, y)
    # print(x)
    # print(y)
    # print(coeficients)
    rezultat1 = func(test_num)
    rezultat2 = solutie_cu_interpolare_geometrica(coeficients, test_num)
    print(rezultat1)
    print(rezultat2)
    # print(abs(rezultat2 - rezultat1))


test1(x3, y3, func3, 1)
print()
test2(x3, y3, func3, 1)
