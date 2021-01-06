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
Num = input(f'Please enter the {enter}')

# ստուգում ենք արդյոք «q» է մուտքագրվել, թե՝ ոչ
while Num != 'q':

    # մուտքագրված թվերը str տիպից դարձնում ենք int-եր պարունակող list
    Num = [int(n) for n in Num.split()]

    # ենթադրում ենք, որ առաջին երկու անդամի արտադրյալը ամենամեծն է
    MP = Num[0] * Num[1]    # առաջին երկու անդամի արտադրյալը
    s = 0                   # առաջին անդամի դիրքը

    # ստուգում ենք՝ արդյոք կա ավելի մեծ արտադրյալով իրար կողք գտնվող երկու էլեմենտ
    for i in range(1, len(Num) - 1):

        # եթե կա, վերագրում ենք այն MP-ին
        if Num[i] * Num[i + 1] > MP:
            MP = Num[i] * Num[i + 1]

            # հիշում ենք տվյալ անդամի տեղը շարքում
            s = i

    # տպում ենք արդյունքը
    answer_counter += 1

    print(f'''
    -ANSWER N{answer_counter}-
    The biggest product is: {MP}
    
    *The product of: {Num[s]} and {Num[s + 1]}
    *At positions: [{s + 1}] and [{s + 2}]
    ''')

    # եթե օգտատերը ուզենա, կարող է մուտքագրել նոր թվեր կամ «q»` ծրագրից դուրս գալու համար
    Num = input(f'If you want to try again, enter new {enter}')

# Goodbye note
print('Thanks for using our program!')
