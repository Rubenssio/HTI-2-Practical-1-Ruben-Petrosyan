def has_only_even_digit(num):
    for i in str(num):
        if int(i) % 2 == 0:
            return False
    return True

    # Classroom version
    # while num != 0:
    #     digit = num % 10
    #
    #     if digit % 2 == 0:
    #         return False
    #
    #     num = num // 10
    #
    # return True


def even_digit_range(start, stop):
    result = []

    for i in range(start, stop):
        if has_only_even_digit(i):
            result.append(i)

    return result


start_stop = [int(n) for n in input('Enter range in format "a-b": ').split('-')]

print(even_digit_range(start_stop[0], start_stop[1]))
# print(has_only_even_digit(int(input('enter: '))))
