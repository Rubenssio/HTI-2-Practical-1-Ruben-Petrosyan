lucky_num = input('Enter the number: ')

first_sum = int()
second_sum = int()

for i in range(int(len(lucky_num) / 2)):
    first_sum += int(lucky_num[i])

for i in range(int(len(lucky_num) / 2), int(len(lucky_num))):
    second_sum += int(lucky_num[i])

if first_sum == second_sum:
    print('Yes')
else:
    print('No')
