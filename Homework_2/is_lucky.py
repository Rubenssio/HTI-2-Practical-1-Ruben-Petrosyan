# վերնագիր
print('''
--- IS LUCKY ---
This program will check whether the entered number is LUCKY
(whether the sum of the first half digits of the number
 is equal to the sum of the digits of the second half)
''')

# տվյալի մուտքագրում
lucky_num = input('Please enter a number with even number of digits: \n')

# հայտարարում ենք փոփոխականները
first_sum = 0
second_sum = 0

# անցնում ենք թվանշանի բոլոր նիշերով
for i in range(len(lucky_num)):

    # գտնում ենք թե թվանշանի որ կեսում է գտնվում տվյալ նիշը
    if i < len(lucky_num) / 2:
        first_sum += int(lucky_num[i])
    else:
        second_sum += int(lucky_num[i])

# արդյյունքի ստուգում և տպում
if first_sum == second_sum:
    print(f'\nYES! The number {lucky_num} is LUCKY\n')
else:
    print(f'\nNo, the number {lucky_num} is NOT LUCKY\n')
