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


list1 = [int(n) for n in input('List 1: ').split()]
list2 = [int(n) for n in input('List 2: ').split()]

print(merge(list1, list2))
