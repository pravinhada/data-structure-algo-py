# use stacke to check the balance

def balance_check(s):

    # edge case check
    if len(s) % 2 != 0:
        return False

    opening = set('([{')  # this will create set of each brackets

    matches = {('(', ')'), ('[', ']'), ('{', '}')}

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0


print(balance_check('[]'))

print(balance_check('{}[]({[()]})'))
print(balance_check('[][({))]'))
