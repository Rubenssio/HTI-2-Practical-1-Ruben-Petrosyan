def input_matrix_and_find(n, to_find):
    mat = []
    loc = 'unknown location'
    for i in range(n):
        row = input().split()
        if to_find in row:
            loc = (i, row.index(to_find))
        mat.append(row)
    return mat, loc


def output_matrix(mtx):
    row = len(mtx)
    col = len(mtx[0])
    for i in range(row):
        for j in range(col):
            print(mtx[i][j], end=' ')
        print()


def transform_diagonal(mat, direction, B_loc):
    for d in direction:
        i = B_loc[0]
        j = B_loc[1]
        while 0 <= i < len(mat) and 0 <= j < len(mat):
            matrix[i][j] = 'x'
            i += d[0]
            j += d[1]

    matrix[B_location[0]][B_location[1]] = 'B'


# MAIN PROGRAM
n = 8

matrix, B_location = input_matrix_and_find(n, 'B')

print('B is at', B_location)

if type(B_location) is not str:
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    transform_diagonal(matrix, directions, B_location)

output_matrix(matrix)
