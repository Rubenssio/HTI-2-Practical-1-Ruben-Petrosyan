# վերնագիր
print('adjacent_elements_product.py')

# տվյալների մուտքագրում
numbers = [int(num) for num in input('Enter the numbers: ').split()]

# ենթադրում ենք, որ առաջին երկու անդամի արտադրյալը ամենամեծն է
max_product = numbers[0] * numbers[1]

# ստուգում ենք՝ արդյոք կա ավելի մեծ արտադրյալով իրար կողք գտնվող երկու էլեմենտ
for i in range(1, len(numbers) - 1):
    product = numbers[i] * numbers[i+1]
    if product > max_product:
        max_product = product

# տպում ենք արդյունքը
print(max_product)
