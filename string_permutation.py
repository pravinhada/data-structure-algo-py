# Recursive example of string permuatation

# for abc -> abc, acb, bac, bca, cab, cba

def permute(s):

    out = []

    # base case
    if len(s) == 1:
        out = [s]

    # for every letter in string
    for i, letter in enumerate(s):
        # for every permutation resulting from step 2 and 32
        for perm in permute(s[:i] + s[i+1:]):
            out += [letter + perm]

    return out


print(permute('abc'))
