print('is_lucky.py')

lucky_num = input('Enter the number: ')

first_sum = 0
second_sum = 0

for i in range(len(lucky_num)):

    if i < len(lucky_num) / 2:
        first_sum += int(lucky_num[i])
    else:
        second_sum += int(lucky_num[i])

if first_sum == second_sum or print('No'):
    print('Yes')
