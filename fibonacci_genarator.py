def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib_gen = fibonacci_generator()
n = int(input("How many numbers would you like to display = "))
for _ in range(n):
    print(next(fib_gen),end=" ")