# վերնագիր
print('is_lucky.py')

# տվյալի մուտքագրում
lucky_num = input('Enter the number: ')

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
    print('Yes')
else:
    print('No')
