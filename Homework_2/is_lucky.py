# վերնագիր
print('''

--- IS LUCKY ---
This program will check whether the entered number is LUCKY
(whether the sum of the digits in the first half of the number
 is equal to the sum of the digits in the second half)
''')

# որ տեսնենք քանի անգամ ենք կոդը աշխատացրել
answer_counter = 0

# տվյալի մուտքագրում
lucky_num = input('Please enter a number with even number of digits, or "q" to quit: \n')

while lucky_num != 'q':

    # միաժամանակ հայտարարում և զրոյացնում ենք փոփոխականները
    first_sum = 0
    second_sum = 0

    # անցնում ենք թվանշանի բոլոր նիշերով
    for i in range(len(lucky_num)):

        # գտնում ենք թե թվանշանի որ կեսում է գտնվում տվյալ նիշը
        if i < len(lucky_num) / 2:
            first_sum += int(lucky_num[i])  # ավելացնում ենք առաջին կեսի գումարին
        else:
            second_sum += int(lucky_num[i])  # կամ ավելիացնում ենք երկրորդ կեսի գումարին

    # արդյյունքի ստուգում և տպում
    answer_counter += 1
    print(f'\n    -ANSWER N{answer_counter}-')
    if first_sum == second_sum:
        print(f'    YES! The number {lucky_num} is LUCKY\n')
    else:
        print(f'    No, the number {lucky_num} is NOT LUCKY\n')

    lucky_num = input('If you want to try again, enter a new number with even number of digits, or "q" to quit: \n')
