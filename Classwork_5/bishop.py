def input_matrix_and_find(n, to_find):
    mat = []
    loc = -1, -1
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


def transform_diagonal(mat, direction, loc):
    for d in direction:
        i = loc[0]
        j = loc[1]
        while 0 <= i < len(mat) and 0 <= j < len(mat):
            matrix[i][j] = 'x'
            i += d[0]
            j += d[1]

    matrix[B_location[0]][B_location[1]] = 'B'


# MAIN PROGRAM
num_of_rows = 8
print('Please input the 8x8 matrix')
matrix, B_location = input_matrix_and_find(num_of_rows, 'B')
print()

if B_location != (-1, -1):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    transform_diagonal(matrix, directions, B_location)
else:
    print("'B' is not found")

output_matrix(matrix)
