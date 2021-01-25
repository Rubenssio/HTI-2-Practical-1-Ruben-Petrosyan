def monotonicity(list1):
    ascending = True
    descending = True

    for i in range(len(list1) - 1):
        if descending and list1[i] <= list1[i + 1]:
            descending = False
        if ascending and list1[i] >= list1[i + 1]:
            ascending = False

    if ascending:
        return 'Ascending'
    if descending:
        return 'Descending'
    return 'Neither'


num_list = [int(n) for n in input('enter the numbers: ').split()]

print(monotonicity(num_list))
