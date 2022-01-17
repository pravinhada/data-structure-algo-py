# base case -> must have this otherwise infinite loop or stack overflow
# recursive case

def funcThree():
    print('Three')


def funcTwo():
    funcThree()
    print('Two')


def funcOne():
    funcTwo()
    print('One')


funcOne()


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))


def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


print(sum([2, 4, 5]))
