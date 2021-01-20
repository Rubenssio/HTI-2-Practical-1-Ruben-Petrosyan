def largest_number(number):
    num = number % 10
    number //= 10
    while number != 0:
        if num > number % 10:
            return 'Yes'
        num = number % 10
        number //= 10

    return 'No'

number = int(input('Enter number: '))

print(largest_number(number))
