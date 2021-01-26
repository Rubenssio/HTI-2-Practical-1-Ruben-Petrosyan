def reverse_list_tail(l, l_rev=[]):
    if not l:
        return l_rev
    return reverse_list_tail(l[:-1], l_rev + [l[-1]])


print(reverse_list_tail([4, 3, 2, 1]))
