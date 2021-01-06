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
    s = [0]                   # առաջին անդամի դիրքը

    # ստուգում ենք՝ արդյոք կա ավելի մեծ արտադրյալով իրար կողք գտնվող երկու էլեմենտ
    for i in range(1, len(Num) - 1):
        P = Num[i] * Num[i + 1]

        # եթե կա, վերագրում ենք այն MP-ին
        if P > MP:
            MP = P

            # հիշում ենք տվյալ անդամի տեղը շարքում
            s = [i]

        # նաև գտնում ենք նույն արտադրյալը ունեցող այլ թվեր
        elif P == MP:
            s.append(i)  # ու հիշում ենք դրանց տեղերը

    # տպում ենք արդյունքը
    answer_counter += 1

    print(f'''
    -ANSWER N{answer_counter}-
    The biggest product is: {MP}
    
    * The product of:''')

    # նաև տպում ենք բոլոր այն դիրքերը, որտեղ գտել ենք ամենամեծ արտադրյալը
    for i in s:
        print(f'      {Num[i]} and {Num[i + 1]} at positions: [{i + 1}] and [{i + 2}]')

    # եթե օգտատերը ուզենա, կարող է մուտքագրել նոր թվեր կամ «q»` ծրագրից դուրս գալու համար
    Num = input(f'\nIf you want to try again, enter new {enter}')

# Goodbye note
print('Thanks for using our program!')
