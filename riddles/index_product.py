# O(n) complexity
# greedy pass forward algorithm

def index_prod(my_list):
    output = [None] * len(my_list)

    product = 1
    i = 0

    while i < len(my_list):
        output[i] = product
        product *= my_list[i]
        i += 1

    print('First forward pass {}'.format(output))

    product = 1
    i = len(my_list) - 1

    while i >= 0:
        output[i] *= product
        product *= my_list[i]
        i -= 1

    return output


print(index_prod([1, 2, 3, 4, 5]))
