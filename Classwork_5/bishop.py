def input_matrix(n):
    mat = []
    for _ in range(n):
        mat.append([el for el in input().split()])
    return mat


def output_matrix(mtx):
    row = len(mtx)
    col = len(mtx[0])
    for i in range(row):
        for j in range(col):
            print(mtx[i][j], end=' ')
        print()


n_of_rows = int(input('Number of rows: '))

matrix = input_matrix(n_of_rows)

# output_matrix(matrix)

num_of_rows = len(matrix)
num_of_cols = len(matrix[0])

B_location = 'unknown location'

found = False
for i in range(num_of_rows):
    for j in range(num_of_cols):
        if matrix[i][j] == 'B':
            B_location = (i, j)
            found = True
            break
    if found:
        break

print('B is at', B_location)

i = B_location[0]
j = B_location[1]
while i >= 0 and j < num_of_cols:
    matrix[i][j] = 'x'
    i -= 1
    j += 1

i = B_location[0]
j = B_location[1]
while i < num_of_rows and j < num_of_cols:
    matrix[i][j] = 'x'
    i += 1
    j += 1

i = B_location[0]
j = B_location[1]
while i < num_of_rows and j >= 0:
    matrix[i][j] = 'x'
    print(i, j)
    i += 1
    j -= 1

i = B_location[0]
j = B_location[1]
while i >= 0 and j >= 0:
    matrix[i][j] = 'x'
    i -= 1
    j -= 1

matrix[B_location[0]][B_location[1]] = 'B'

output_matrix(matrix)