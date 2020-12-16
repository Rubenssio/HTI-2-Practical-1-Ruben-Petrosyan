n1 = input()
n2 = input()
N = input()

n1 = int(n1)
n2 = int(n2)
N = int(N)

step = n2 - n1
nN = n1 + (N - 1) * step

print(f'[{N}] = {nN}')