# n = n + (n-1) + (n-2) ..... 3+2+1
def recursive_sum(n):
    # base case
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


print(recursive_sum(4))


# 4321 = 4+3+2+1 = 10
def sum_recursive(n):
    # base case
    if len(str(n)) == 1:
        return n

    return n % 10 + sum_recursive(n // 10)


print(sum_recursive(4321))


def word_split(phrase, list_of_words, output=None):
    if output is None:
        return []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word):], list_of_words, output)

    return output


print(word_split('themanran', ['man', 'ran', 'man', 'dog', 'the', 'woman'], []))
