'''from numpy import matrix

m = matrix('1 2; 3 4; 5 6')
print(m)

m.reshape(3,2)'''


def rotate(matrix):
    return [[matrix[j][i] for j in range(len(matrix) - 1, -1, -1)] for i in range(len(matrix))]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in rotate(matrix):
    print(row)

    

def rotate():
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix) -1,-1,-1)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in rotate():
    print(row)



8
