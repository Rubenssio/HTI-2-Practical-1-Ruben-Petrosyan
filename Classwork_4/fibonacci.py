def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    fib1 = 1
    fib2 = 1
    for _ in range (n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1

num = int(input('Enter a number: '))
print(fibonacci(num - 1))

# assuming user starts counting from 1, not from 0
# thus the last line is: print(fibonacci(num - 1))
# the fibonacci() function still returns what you would expect
