def number_root(num):
    while num // 10 != 0:
        root = 0
        while num != 0:
            root += num % 10
            num //= 10
        num, root = root, 0

    return num


print(number_root(int(input("Enter the number: "))))
