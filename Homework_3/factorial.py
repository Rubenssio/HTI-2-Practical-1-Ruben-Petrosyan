def factorial(number):
    """Returns the factorial of the given number"""
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


print(factorial(int(input('Enter the number: '))))
