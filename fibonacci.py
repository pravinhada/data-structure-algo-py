# Fibonacci Sequence using recursive

def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(10))


# Fibonacci Sequence using iterative

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


print(fibonacci_iterative(10))

# Fibonacci Sequence using dynamic programming
n1 = 10
cache = [None] * (n1 + 1)


def fibonacci_dynamic(n):
    if n == 0 or n == 1:
        return n

    if cache[n] is not None:
        return cache[n]

    cache[n] = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)
    return cache[n]


print(fibonacci_iterative(10))
