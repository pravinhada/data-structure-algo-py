import sys

# egg drop interview question riddle for n eggs with k floors
# time complexity is exponential

def egg_drop(n, k):

    if k == 1 or k == 0:
        return k

    if n == 1:
        return k

    min = sys.maxsize

    for x in range(1, k+1):
        res = max(egg_drop(n-1, x-1), egg_drop(n, k-x))

        if res < min:
            min = res

    return min + 1


# n = number of eggs, k = number of floors
n = 2
k = 10

print('minimum number of trials in worst case with {} eggs and {} floors is {}'.format(
      n, k, egg_drop(n, k)))
