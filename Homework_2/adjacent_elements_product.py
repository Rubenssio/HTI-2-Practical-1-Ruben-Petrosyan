# վերնագիր
print('''

--- ADJACENT ELEMENTS PRODUCT ---
This program will return the biggest product of
the adjacent elements from the entered sequence
''')

# որ տեսնենք քանի անգամ ենք կոդը աշխատացրել
answer_counter = 0

# մուտքագրելուց ցուցադրվող տեքստը
enter = 'numbers separated with spaces, or "q" to quit: \n'

# տվյալների մուտքագրում
# ակնկալում ենք բացատներով առանձնացված թվեր կամ «q»՝ ծրագրից դուրս գալու համար
N = input(f'Please enter the {enter}')

# երկու թվի արտադրյալ հաշվելու համար։ P-ն product բառից
P = lambda x, y: x * y

# ստուգում ենք արդյոք «q» է մուտքագրվել, թե՝ ոչ
while N != 'q':

    # մուտքագրված թվերը str տիպից դարձնում ենք int-եր պարունակող list
    N = [int(num) for num in N.split()]

    # ենթադրում ենք, որ առաջին երկու անդամի արտադրյալը ամենամեծն է
    max_product = N[0] * N[1]
    n1 = [N[0], 1]
    n2 = [N[1], 2]

    # ստուգում ենք՝ արդյոք կա ավելի մեծ արտադրյալով իրար կողք գտնվող երկու էլեմենտ
    for i in range(1, len(N) - 1):

        if P(N[i],N[i + 1]) > max_product:
            max_product = P(N[i],N[i + 1])

            # հիշում ենք տվյալ թվերը և դրանց տեղը շարքում
            n1 = [N[i], i + 1]
            n2 = [N[i + 1], i + 2]

    # տպում ենք արդյունքը
    answer_counter += 1
    print(f'''
    -ANSWER N{answer_counter}-
    The biggest product is: {max_product}
    
    it's the product of numbers {n1[0]} and {n2[0]}
    which are on positions [{n1[1]}] and [{n2[1]}]
    ''')

    # եթե օգտատերը ուզենա, կարող է նոր թվեր մուտքագրել կամ սեղմել «q»` ծրագրից դուրս գալու համար
    N = input(f'If you want to try again, enter new {enter}')
