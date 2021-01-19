def factorial(number):
    if number == 0 or number == 1:
        fact = 1
    else:
        fact = number * factorial(number - 1)

    return fact


print(factorial(int(input('Enter the number: '))))
