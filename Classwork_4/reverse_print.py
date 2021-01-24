def reverse_print(n):
    if not n:
        return
    x = int(input())
    reverse_print(n-1)
    print(x)


n = int(input('n = '))
reverse_print(n)
