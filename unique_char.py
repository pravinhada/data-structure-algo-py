# simple solution
def unique_char1(s):
    return len(set(s)) == len(s)


def unique_char2(s):
    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)

    return True


print(unique_char1('abcdef'))
print(unique_char1('abcdefe'))

print(unique_char2('abcdef'))
print(unique_char2('abcdefe'))
