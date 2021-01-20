def missing_number(numbers):

    for el in range(1, len(numbers) + 2):
        if el not in numbers:
            return el


num = [int(n) for n in input("Enter the numbers: ").split()]

print(missing_number(num))
