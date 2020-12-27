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
numbers = input(f'Please enter the {enter}')

# ստուգում ենք արդյոք «q» է մուտքագրվել, թե՝ ոչ
while numbers != 'q':

    # մուտքագրված թվերը str տիպից դարձնում ենք int-եր պարունակող list
    numbers = [int(num) for num in numbers.split()]

    # ենթադրում ենք, որ առաջին երկու անդամի արտադրյալը ամենամեծն է
    max_product = numbers[0] * numbers[1]
    n1 = [numbers[0], 1]
    n2 = [numbers[1], 2]

    # ստուգում ենք՝ արդյոք կա ավելի մեծ արտադրյալով իրար կողք գտնվող երկու էլեմենտ
    for i in range(1, len(numbers) - 1):

        product = numbers[i] * numbers[i + 1]
        if product > max_product:
            max_product = product

            # հիշում ենք տվյալ թվերը և դրանց տեղը շարքում
            n1 = [numbers[i], i + 1]
            n2 = [numbers[i + 1], i + 2]

    # տպում ենք արդյունքը
    answer_counter += 1
    print(f'''
    -ANSWER N{answer_counter}-
    The biggest product is: {max_product}
    
    it's the product of numbers {n1[0]} and {n2[0]}
    which are on positions [{n1[1]}] and [{n2[1]}]
    ''')

    # եթե օգտատերը ուզենա, կարող է նոր թվեր մուտքագրել կամ սեղմել «q»` ծրագրից դուրս գալու համար
    numbers = input(f'If you want to try again, enter new {enter}')
