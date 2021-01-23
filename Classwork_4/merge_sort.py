def merge(l1, l2):
    i = j = 0

    l_merged = []

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l_merged.append(l1[i])
            i += 1
        else:
            l_merged.append(l2[j])
            j += 1

    l_merged.extend(l1[i:] + l2[j:])
    # l_merged + l1[i:] + l2[j:]

    return l_merged


def merge_sort(numbers, start, end):
    if start == end - 1:
        return numbers[start:end]

    mid = (start + end) // 2

    a = merge_sort(numbers, start, mid)
    b = merge_sort(numbers, mid, end)

    return merge(a, b)


numbers = [int(n) for n in input('Numbers: ').split()]

print(merge_sort(numbers, 0, len(numbers)))
