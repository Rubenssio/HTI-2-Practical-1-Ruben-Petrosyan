def missing_number(numbers):
    biggest = max(numbers)
    smallest = min(numbers)

    for el in range(smallest, biggest):
        if el not in numbers:
            return el

num = [int(n) for n in input("Enter the numbers: ").split()]

print(missing_number(num))
