import copy

def store_matrix(filename):
    first = True
    with open(filename, 'r') as matrix:
        for line in matrix:
            if first:
                n = int(line)
                first = False
                vector = [[] for i in range(n)]
            else:
                elements = line.split()
                el = float(elements[0][:-1])
                i = int(elements[1][:-1])
                j = int(elements[2])
                not_found = True
                for index, tup in enumerate(vector[i]):
                    if tup[1] == j:
                        vector[i][index] = (tup[0] + el, tup[1])
                        not_found = False
                if not_found:
                    vector[i].append((el, j))
    return(vector)

def matrix_sum(a,b):
    sum_vector = copy.deepcopy(a)
    for line_num, i in enumerate(b):
        for j in i:
            not_found = True
            for index, tup in enumerate(sum_vector[line_num]):
                if tup[1] == j[1]:
                    sum_vector[line_num][index] = (tup[0] + j[0], tup[1])
                    not_found = False
                    break
            if not_found:
                sum_vector[line_num].append(j)
    return sum_vector

def matrix_product(a,b):
    b_column_matrix = {n: [] for n in range(len(b))}
    for line_num, i in enumerate(b):
        for j in i:
            b_column_matrix[j[1]].append((j[0], line_num))
    product_matrix = [[] for i in range(len(b))]
    for line_num, i in enumerate(a):
        for col_number_b in range(len(b_column_matrix)):
            product_elem = 0
            for j in i:
                for k in b_column_matrix[col_number_b]:
                    if j[1] == k[1]:
                        product_elem += k[0] * j[0]
                        break
            if product_elem != 0:
                product_matrix[line_num].append((product_elem, col_number_b))
    return product_matrix

def compare_vectors(a,b):
    for line_num, i in enumerate(a):
        for j in i:
            not_found = True
            for tup in b[line_num]:
                if tup == j:
                    not_found = False
                    break
            if not_found:
                return False
    return True

a = store_matrix("a.txt")
b = store_matrix("b.txt")
sum = matrix_sum(a, b)
check_sum = store_matrix("sum.txt")
prod = matrix_product(a, b)
check_prod = store_matrix("prod.txt")
print(prod)
print(compare_vectors(prod, check_prod))