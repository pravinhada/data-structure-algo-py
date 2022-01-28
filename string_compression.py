def str_compress(s):
    result = ''
    l = len(s)

    if l == 0:
        return ''

    if l == 1:
        return s+'1'

    last = s[0]
    count = 1
    i = 1

    while i < l:
        if s[i] == s[i-1]:
            count += 1
        else:
            result = result + s[i-1] + str(count)
            count = 1

        i += 1

    result = result + s[i-1]+str(count)

    return result


print(str_compress('AAAbbbbbbccccDDDDD'))