print('\nCreate an ARITHMETIC PROGRESSION by entering the first two members of the sequence!')
n1 = int(input('Please enter the first member of the progression: '))
n2 = int(input('Please enter the second member of the progression: '))
N = int(input('\nWhich member of this progression would you like to see?\nPlease enter the N: '))

step = n2 - n1
nN = n1 + (N - 1) * step

print(f'[{N}] = {nN}')
