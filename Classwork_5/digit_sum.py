def digit_sum(num):
    if num == 0:
        return 0

    return num % 10 + digit_sum(num// 10)


print(digit_sum(int(input('Enter number: '))))
