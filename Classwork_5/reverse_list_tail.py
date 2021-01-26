def reverse_list_tail(l, l_rev=[]):
    if not l:
        return l_rev
    l_rev.append(l[-1])
    return reverse_list_tail(l[:-1], l_rev)


print(reverse_list_tail([4, 3, 2, 1]))
