from collections import deque


# simple but not for interview

def reverse_sentence1(sen):
    return ' '.join(reversed(sen.split()))


# using algorithmic way

def reverse_sentence2(sen):
    words = []
    length = len(sen)
    space = [' ']

    i = 0

    while i < length:
        if sen[i] not in space:
            word_start = i

            while i < length and sen[i] not in space:
                i += 1

            words.append(sen[word_start:i])

        i += 1

    return ' '.join(reverse(words))


def reverse(words):
    stack = deque()
    result = []

    for word in words:
        stack.append(word)

    for _ in range(len(stack)):
        result.append(stack.pop())

    return result


s = 'company and job types'
sol = reverse_sentence2(s)
print(s)
print(sol)
