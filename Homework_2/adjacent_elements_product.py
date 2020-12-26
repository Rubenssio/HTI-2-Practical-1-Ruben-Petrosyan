# վերնագիր
print('''

--- ADJACENT ELEMENTS PRODUCT ---
This program will return the biggest product of
the adjacent elements from the entered sequence
''')

# տվյալների մուտքագրում
numbers = [int(num) for num in input('Please enter the numbers separated with spaces: \n').split()]

# ենթադրում ենք, որ առաջին երկու անդամի արտադրյալը ամենամեծն է
max_product = numbers[0] * numbers[1]
n1 = [numbers[0], 1]
n2 = [numbers[1], 2]

# ստուգում ենք՝ արդյոք կա ավելի մեծ արտադրյալով իրար կողք գտնվող երկու էլեմենտ
for i in range(1, len(numbers) - 1):

    product = numbers[i] * numbers[i+1]
    if product > max_product:
        max_product = product

        # հիշում ենք տվյալ թվերը և դրանց տեղը շարքում
        n1 = [numbers[i], i+1]
        n2 = [numbers[i+1], i+2]

# տպում ենք արդյունքը
print(f'''
-ANSWER-
The biggest product is: {max_product}

it's the product of {n1[0]} and {n2[0]}
which are on positions [{n1[1]}] and [{n2[1]}]
''')
