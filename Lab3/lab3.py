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
                vector[i].append((el, j))
    return (vector)

print(store_matrix("a.txt"))