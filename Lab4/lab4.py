epsilon = 10 ** -16

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
    for i in vector:
        if len(i) > 11:
            raise ValueError('Too many elements per line!')
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

def keep_vector(filename):
    #similar cu metoda de mai sus dar pentru un vector
    return_vector = list()
    first = True
    with open(filename, 'r') as vector:
        for line in vector:
            if first:
                first = False
            else:
                return_vector.append(float(line))
    return return_vector

def gauss_sindel(matrix, vector):
    xGS = [0 for i in range(len(vector))]
    k = 0
    kmax = 10000
    delta = 1
    while delta >= epsilon and k <= kmax and delta <= (10 ** 8):
        delta = 0
        #parcurg vectorul xGS
        for i in range(len(xGS)):
            #aici voi retine elmentul de pe diagonala pt a imparti la el mai tarziu
            diag_element = 0
            #retin elementul vechi pt a putea face calcule cu el dupa ce il inlocuiesc in xGS
            old_elem = xGS[i]
            #mai intai adaug b, dupa in timp ce parcurg a scad din b si la sfarsit impart la elementul de pe diagonala
            new_elem = vector[i]
            #parcurg o linie din matrice
            for j in matrix[i]:
                #daca este element pe diagonala principala
                if j[1] == i:
                    diag_element = j[0]
                else:
                    # aici nu trebuie sa fac cate un caz daca j e mai mic sau mai mare decat i, deoarece elementele
                    # sunt inlocuite iterativ, deci daca j este mai mic, vor fi elemente din x(k+1) in xGS, iar daca
                    # j este mai mare, elemntele din xGS vor fi x(k)
                    new_elem -= j[0]*xGS[i]
            new_elem = new_elem / diag_element
            xGS[i] = new_elem
            #calculul normei?
            if (new_elem - old_elem) > delta:
                delta = (new_elem - old_elem)
        k += 1
        print(k)
    if(delta < epsilon):
        return xGS
    else:
        print("Divergenta")



a = keep_matrix("a5.txt")
b = keep_vector("b5.txt")
print(gauss_sindel(a, b))