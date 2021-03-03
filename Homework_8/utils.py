import sys


def all_odd_digits(num):
    """
    Checks whether all the digits of the number are odd

    Parameters
    ----------
    num : int
        the number to check

    Returns
    -------
    bool
        True, if all digits in the number are odd
        False, if number has one or more even digits
    """

    for char in str(num):
        if int(char) % 2 == 0:
            return False
    return True


def odd_gen(start, stop):
    """
    Generates numbers between start and stop (noninclusive)
    consisting of only even digits

    Parameters
    ----------
    start : int
        the starting point of the sequence
    stop : int
        the end of the sequence (noninclusive)

    Yields
    ------
    int
        next number between start and stop (noninclusive)
        consisting of only even digits
    """

    if start % 2 == 0:
        current_num = start + 1
    else:
        current_num = start

    while current_num < stop:
        if all_odd_digits(current_num):
            yield current_num
        current_num += 2


if __name__ == '__main__':

    successful_a_b_assignment = False

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        successful_a_b_assignment = True

    except (IndexError, ValueError):
        print('\nThis program works only with two command line arguments the type of which are "int"\n')

    if successful_a_b_assignment:
        for n in odd_gen(a, b):
            print(n, end=' ')
        print('\n')
