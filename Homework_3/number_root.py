def number_root(num):
    """Adds the digits of the given number,
    then does the same thing to the result,
    and so on until the result is a single digit number.
    Returns the single digit number"""

    if num <= 9:
        return num

    root = 0
    while num != 0:
        root += num % 10
        num //= 10

    return number_root(root)


print(number_root(int(input("Enter the number: "))))
