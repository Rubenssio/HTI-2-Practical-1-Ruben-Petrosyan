def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 'No'
    return 'Yes'


print(is_prime(int(input("Enter the number: "))))
