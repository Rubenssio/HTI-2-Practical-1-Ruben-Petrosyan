# վերնագիր
print('''

--- ADJACENT ELEMENTS PRODUCT ---
This program will return the biggest product of
two adjacent elements from the entered sequence
''')

# որ տեսնենք քանի անգամ ենք կոդը աշխատացրել
answer_counter = 0

# մուտքագրելուց ցուցադրվող տեքստը
enter = 'numbers separated with spaces, or "q" to quit: \n'

# տվյալների մուտքագրում
# ակնկալում ենք բացատներով առանձնացված թվեր կամ «q»՝ ծրագրից դուրս գալու համար
N = input(f'Please enter the {enter}')

# երկու թվի արտադրյալ հաշվելու համար։ P-ն product բառից
# անտեսում եմ code checker-ի՝ lambda-ն def դարձնելու պահանջը
P = lambda x, y: x * y

# ստուգում ենք արդյոք «q» է մուտքագրվել, թե՝ ոչ
while N != 'q':

    # մուտքագրված թվերը str տիպից դարձնում ենք int-եր պարունակող list
    N = [int(num) for num in N.split()]

    # ենթադրում ենք, որ առաջին երկու անդամի արտադրյալը ամենամեծն է
    MP = N[0] * N[1]  # MP = Max_Product
    s = 0  # s = the position of the first element from MP

    # ստուգում ենք՝ արդյոք կա ավելի մեծ արտադրյալով իրար կողք գտնվող երկու էլեմենտ
    for i in range(1, len(N) - 1):

        if P(N[i], N[i + 1]) > MP:
            MP = P(N[i], N[i + 1])

            # հիշում ենք տվյալ թվի տեղը շարքում
            s = i

    # տպում ենք արդյունքը
    answer_counter += 1

    print(f'''
    -ANSWER N{answer_counter}-
    The biggest product is: {MP}
    
    *The product of: {N[s]} and {N[s + 1]}
    *At positions: [{s + 1}] and [{s + 2}]
    ''')

    # եթե օգտատերը ուզենա, կարող է նոր թվեր մուտքագրել կամ սեղմել «q»` ծրագրից դուրս գալու համար
    N = input(f'If you want to try again, enter new {enter}')
