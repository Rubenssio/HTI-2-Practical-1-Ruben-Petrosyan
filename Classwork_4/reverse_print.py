def reverse_print(n):
    if n == 0:
        return ""
    x = int(input())
    reverse_print(n-1)
    print(x)


reverse_print(5)
