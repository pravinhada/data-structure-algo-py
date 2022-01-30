# Fibonnaci Sequence using recursive

def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_recursive(10))


# Fibonacci Sequence using iterative

def fibonnaci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b

    return a


print(fibonnaci_iterative(10))


# Fibonacci Sequence using dynamic programming
n = 10
cache = [None] * (n+1)


def fibonnaci_dynamic(n):
    if n == 0 or n == 1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fibonnaci_dynamic(n-1) + fibonnaci_dynamic(n-2)
    return cache[n]


print(fibonnaci_iterative(10))