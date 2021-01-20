def stools(height_list):
    tallest = max(height_list)
    sum = 0
    for el in height_list:
        sum += tallest - el

    return sum


numbers = [int(n) for n in input("Enter the numbers: ").split()]

print(stools(numbers))
