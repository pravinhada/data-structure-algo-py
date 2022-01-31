# base case -> must have this otherwise infinite loop or stack overflow
# recursive case

def func_three():
    print('Three')


def func_two():
    func_three()
    print('Two')


def func_one():
    func_two()
    print('One')


func_one()


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(4))


def recursive_sum(arr):
    if not arr:
        return 0
    return arr[0] + recursive_sum(arr[1:])


print(recursive_sum([2, 4, 5]))


def reverse_string(s):
    # base case
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


print(reverse_string('hello world'))
