def is_prime(num):
    """Gets a number and checks whether it's a prime number

    Parameters
    ----------
    num : int
        The number to check

    Returns
    -------
    bool
        True  - if the given number IS prime,
        False - if the given number IS NOT prime
    """

    if num == 2:
        return True

    if num % 2 == 0 or num == 1:
        return False

    for i in range(3, num//2 + 1, 2):
        if num % i == 0:
            return False
    return True


def goldbach_s_conjecture(even_num):
    """Gets an even number and returns a list of prime number pairs
    where the sum of each pair is equal to the given number

    Parameters
    ----------
    even_num : int
        an even integer to check

    Returns
    -------
    list
        a list of prime number pairs where the sum
        of each pair is equal to the given number
    """

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


# THE MAIN PROGRAM
print("""\n        ***GOLDBACH's conjecture***
Conjecture states that every even whole number
greater than 2 is a sum of two prime numbers
""")

user_input = 'even number bigger than 2 to find\nwhich two primes make up that number\n: '


number = int(input(f'Enter an {user_input}'))

GC_primes = goldbach_s_conjecture(number)

if type(GC_primes) != list:
    print(GC_primes)
else:
    print(f"""    According to Goldbach's conjecture, number {number}
    can be expressed as the sum of the following numbers:
    """)
    for prime_pair in GC_primes:
        print(f'{prime_pair[0]:>8} {prime_pair[1]}')
