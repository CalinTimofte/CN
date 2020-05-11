import random
import copy
import numpy
epsilon = 10 ** -9
kmax = 1000000

def keep_matrix(filename):
    #asta este bucata de cod de datat trecuta, modificata sa mearga oriunde ar fi ","
    first = True
    with open(filename, 'r') as matrix:
        for line in matrix:
            if first:
                n = int(line)
                first = False
                vector = [[] for i in range(n)]
            else:
                elements = line.split(",")
                for ii in range(3):
                    elements[ii] = elements[ii].replace(" ", "")
                el = float(elements[0])
                i = int(elements[1])
                j = int(elements[2])
                not_found = True
                for index, tup in enumerate(vector[i]):
                    if tup[1] == j:
                        vector[i][index] = (tup[0] + el, tup[1])
                        not_found = False
                if not_found:
                    vector[i].append((el, j))
    # for i in vector:
    #     if len(i) > 11:
    #         raise ValueError('Too many elements per line!')
    #bucata asta de functie verifica daca exita elemente pe diagonala principala
    return_vector = vector
    n = len(return_vector)
    for line_num, i in enumerate(return_vector):
        first_diagonal_element_found = False
        for j in i:
            if j[1] == line_num:
                if abs(j[0]) > epsilon:
                    first_diagonal_element_found = True
        if first_diagonal_element_found == False:
            raise ValueError('First diagonal is not full!')
    return return_vector

def generate_rare_symmetric_matrix(n, max_int):
    generated_matrix = list()
    filled_indexes = list()
    for i in range(n):
        generated_matrix.append(list())
        filled_indexes.append(list())
        generated_matrix[i].append((random.randint(1, max_int-1), i))
        filled_indexes[i].append(i)
    for i in range(n):
        #add a random number of elements to a line
        for nb_elem in range(random.randint(0, (n/4)-1)):
            # generate j:
            j = random.randint(0, n-1)
            #check j:
            if j != i and j not in filled_indexes[i]:
                #add the element with indexes ij but also ji
                value = random.randint(1, max_int-1)
                generated_matrix[i].append((value, j))
                filled_indexes[i].append(j)
                generated_matrix[j].append((value, i))
                filled_indexes[j].append(i)
    return generated_matrix

def simetry_check(matrix):
    found = False
    for nr_linie, i in enumerate(matrix):
        for j in i:
            if j[1] != nr_linie:
                for search_elem in matrix[j[1]]:
                    if search_elem[0] - j[0] <= epsilon and search_elem[1] == nr_linie:
                        found = True
                if found == False:
                    return False
                else:
                    found = False
    return True

def euclidian_norm(x, is_vector):
    euclidian_norm = 0
    if is_vector:
        new_list = list()
        new_list.append(x)
        x = new_list
    for nr_line, i in enumerate(x):
        for j in i:
            euclidian_norm += j[0] ** 2
    euclidian_norm = euclidian_norm ** 0.5
    return euclidian_norm

def multiply_matrix_with_scalar(x, is_vector, scalar):
    if is_vector:
        new_list = list()
        new_list.append(x)
        x = new_list
    return_matrix = [[] for i in x]
    for nr_line, i in enumerate(x):
        for j in i:
            return_matrix[nr_line].append((j[0] * scalar, j[1]))
    if is_vector:
        new_list = copy.deepcopy(return_matrix[0])
        return_matrix = list()
        return_matrix = copy.deepcopy(new_list)
    return return_matrix

def vector_matrix_multiplication(vector, matrix):
    return_vector = list()
    for i in vector:
        element = 0
        for j in matrix[i[1]]:
            element += j[0] * i[0]
        return_vector.append((element, i[1]))
    return return_vector

def scalar_multiplication(a, b):
    return_value = 0
    if len(a) < len(b):
        small_vector = a
        big_vector = b
    else:
        small_vector = b
        big_vector = a
    column_values = list()
    for i in big_vector:
        column_values.append(i[1])
    for i in small_vector:
        if i[1] in column_values:
            for j in big_vector:
                if i[1] == j[1]:
                    return_value += i[0] * j[0]
    return return_value

def generate_vector_with_euclidian_norm_1(n, max_val):
    return_vector = list()
    column_values = list()
    for i in range(1, random.randint(0, n-1)):
        column = random.randint(0, n-1)
        if column not in column_values:
            column_values.append(column)
            return_vector.append((random.randint(0, max_val-1), column))
    norm = euclidian_norm(return_vector, True)
    norm = 1/norm
    return_vector = multiply_matrix_with_scalar(return_vector, True, norm)
    return return_vector

def vector_minus_vector(a, b):
    return_vector = list()
    for i in b:
        return_vector.append((0-i[0], i[1]))
    for i in a:
        found = False
        for nb_elem, j in enumerate(return_vector):
            if i[1] == j[1]:
                return_vector[nb_elem] = (return_vector[nb_elem][0] + i[0], return_vector[nb_elem][1])
                found = True
        if found == False:
            return_vector.append((i[0], i[1]))
    return return_vector

#aprox 2020 pt toate fisierele
def metoda_puterii(matrix):
    local_epsilon = epsilon
    v = generate_vector_with_euclidian_norm_1(len(matrix), 1000)
    w = vector_matrix_multiplication(v, matrix)
    lambd = scalar_multiplication(w, v)
    k = 0
    while True:
        v = multiply_matrix_with_scalar(w, True, (1/euclidian_norm(w, True)))
        w = vector_matrix_multiplication(v, matrix)
        lambd = scalar_multiplication(w, v)
        k += 1
        if euclidian_norm(vector_minus_vector(w, multiply_matrix_with_scalar(v, True, lambd)), True) > len(matrix) * epsilon:
            return (lambd, v)
        if k >= kmax:
            local_epsilon *= 10
            v = generate_vector_with_euclidian_norm_1(len(matrix), 1000)
            w = vector_matrix_multiplication(v, matrix)
            lambd = scalar_multiplication(w, v)
            k = 0

def print_func(filename):
    x = keep_matrix(filename)
    print(simetry_check(x))
    print(metoda_puterii(x)[0])
    print()

def punctul2():
    a = generate_rare_symmetric_matrix(100, 100000)
    print(simetry_check(a))
    print(metoda_puterii(a)[0])
    print()

    print_func("a300.txt")
    print_func("a500.txt")
    print_func("a1000.txt")
    print_func("a1500.txt")
    print_func("a2020.txt")

def punctul3():
    A = numpy.random.rand(50,50)

    SVD = numpy.linalg.svd(A)
    singular_values = SVD[1]
    #valori singulare
    print(singular_values)
    print()

    #rang
    print(numpy.linalg.matrix_rank(A))
    print()

    #nr de conditionare
    print(numpy.linalg.cond(A))
    print()

    #pseudo-inversa Moore-Penrose
    print(numpy.linalg.pinv(A))
    print()

    # solving the system
    b = numpy.random.rand(50)
    x = numpy.linalg.solve(A, b)
    norma = numpy.linalg.norm(b-A.dot(x),2)
    print(norma)
    print()

    Ainv = numpy.matmul(numpy.transpose(A),A)
    Ainv = numpy.linalg.inv(Ainv)
    PSM = numpy.matmul(Ainv, numpy.transpose(A))
    PSMnorm = numpy.linalg.norm(numpy.subtract(numpy.linalg.pinv(A) , PSM), 1)
    print(PSMnorm)
    print()



punctul2()
# punctul3()
# print_func("a1000.txt")