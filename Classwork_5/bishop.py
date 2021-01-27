def input_matrix(n):
    mat = []
    loc = 'unknown location'
    for i in range(n):
        row = input().split()
        if 'B' in row:
            loc = (i, row.index('B'))
        mat.append(row)

    return mat, loc


def output_matrix(mtx):
    row = len(mtx)
    col = len(mtx[0])
    for i in range(row):
        for j in range(col):
            print(mtx[i][j], end=' ')
        print()


#MAIN PROGRAM
n_of_rows = int(input('Number of rows: '))

matrix, B_location = input_matrix(n_of_rows)

num_of_rows = len(matrix)
num_of_cols = len(matrix[0])

print('B is at', B_location)

if type(B_location) is not str:
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dir in directions:
        i = B_location[0]
        j = B_location[1]
        while 0 <= i < num_of_rows and 0 <= j < num_of_cols:
            matrix[i][j] = 'x'
            i += dir[0]
            j += dir[1]

    matrix[B_location[0]][B_location[1]] = 'B'

    output_matrix(matrix)
