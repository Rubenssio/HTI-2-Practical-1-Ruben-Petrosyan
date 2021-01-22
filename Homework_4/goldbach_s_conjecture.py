def is_prime(num):
    """Checks whether the given number is a prime number
    and returns True or False accordingly:
        True  - if the given number IS prime,
        False - if the given number IS NOT prime"""

    if num == 2:
        return True

    if num % 2 == 0 or num == 1:
        return False

    for i in range(3, num//2 + 1, 2):
        if num % i == 0:
            return False
    return True


def goldbach_s_conjecture(even_num):
    if even_num < 3:
        return f'The number {even_num} is not bigger than 2'

    if even_num % 2 != 0:
        return f'The number {even_num} is not even'

    if even_num == 4:
        return [(2, 2)]

    about_quarter = even_num // 4 + even_num // 2 % 2

    goldbach_primes = []

    for i in range(1, about_quarter):
        a = i * 2 + 1
        b = even_num - a
        if is_prime(a) and is_prime(b):
            goldbach_primes.append((a, b))

    return goldbach_primes


# THE START OF THE PROGRAM
print("""\n        ***GOLDBACH's conjecture***
Conjecture states that every even whole number
greater than 2 is the sum of two prime numbers
""")

user_input = 'even number bigger than 2, to find which two primes makes that number\n: '


num = int(input(f'Enter an {user_input}'))

GC = goldbach_s_conjecture(num)

if type(GC) != list:
    print(GC)
else:
    print(f"""    According to Goldbach's conjecture, number {num}
    can be expressed as the sum of the following numbers:
    """)
    for el in GC:
        print('    ', el[0], el[1])
