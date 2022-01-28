import collections

# first solution


def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


# second solution

def finder2(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


# third solution

def finder3(arr1, arr2):
    result = 0

    for num in arr1+arr2:
        result ^= num

    return result


arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]

print(finder(arr1, arr2))
print(finder2(arr1, arr2))
print(finder3(arr1, arr2))