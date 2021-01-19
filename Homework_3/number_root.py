def number_root(num):
    """Adds the digits of the given number,
    then adoes the same thing to the result,
    and so on until the result is a single digit number.
    Returns the single digit number"""

    while num // 10 != 0:
        root = 0
        while num != 0:
            root += num % 10
            num //= 10
        num, root = root, 0

    return num


print(number_root(int(input("Enter the number: "))))
