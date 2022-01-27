
# simple version, not preferred
def anagram1(string1, string2):
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()
    return sorted(string1) == sorted(string2)


# more preferred version
def anagram2(string1, string2):
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()

    if len(string1) != len(string2):
        return False

    count = {}

    for letter in string1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in string2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


print(anagram1('dog', 'god'))
print(anagram1('aa', 'bb'))

print(anagram2('clint eastwood', 'old west action'))