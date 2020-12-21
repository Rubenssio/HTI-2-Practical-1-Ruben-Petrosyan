# վերնագիր
print('\nCreate an ARITHMETIC PROGRESSION by entering the first two members of the sequence!')

# տվյալների մուտքագրում user-ի կողմից
n1 = int(input('Please enter the first member of the progression: '))
n2 = int(input('Please enter the second member of the progression: '))
N = int(input('\nWhich member of this progression would you like to see?\nPlease enter the N: '))

# ԳԼԽԱՎՈՐ ԿՈԴԸ
step = n2 - n1  # գտնում ենք պրոգրեսիայի քայլը
nN = n1 + (N - 1) * step  # գտնում ենք N-րդ անդամը

# արդյունքի տպում
print('\n-Answer-\nThe N-th member of this progression is:')
print(f'[{N}] = {nN}\n')
