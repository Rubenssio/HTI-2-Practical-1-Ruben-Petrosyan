def binary_search(numbers, target, start, end):
    if start >= end:
        return False

    half_index = (start + end) // 2

    if target == numbers[half_index]:
        return True

    if target < numbers[half_index]:
        return binary_search(numbers, target, start, half_index)

    return binary_search(numbers, target, half_index + 1, end)


print(binary_search([2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37], target=9, start=0, end=16))
