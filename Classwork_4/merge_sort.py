def merge(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    i = j = 0

    l_merge = []

    while i < len1 and j < len2:
        if l1[i] < l2[j]:
            l_merge.append(l1[i])
            i += 1
        else:
            l_merge.append(l2[j])
            j += 1

    l_merge.extend(l1[i:] + l2[j:])

    return l_merge


list1 = [int(n) for n in input('List 1: ').split()]
list2 = [int(n) for n in input('List 2: ').split()]

print(merge(list1, list2))
