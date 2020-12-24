numbers = [int(num) for num in input('Enter the numbers: ').split()]

max_product = numbers[0] * numbers[1]

for i in range(1, len(numbers) - 1):
    product = numbers[i] * numbers[i+1]
    if product > max_product:
        max_product = product

print(max_product)
