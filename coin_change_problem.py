# below recursive_change is not efficient
def recursive_coin(target, coins):

    min_coin = target

    if target in coins:
        return 1

    for i in [c for c in coins if c <= target]:
        num_coins = 1 + recursive_coin(target - i, coins)

        if num_coins < min_coin:
            min_coin = num_coins

    return min_coin


print(recursive_coin(10, [1, 5, 10]))


# dynamic programming to solve the above problem

def recursive_coin_dynamic(target, coins, known_results):

    # default output to target
    min_coins = target

    # base case
    if target in coins:
        known_results[target] = 1
        return 1

    # return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + \
                recursive_coin_dynamic(target-i, coins, known_results)

            if num_coins < min_coins:
                min_coins = num_coins

                # reset that known result
                known_results[target] = min_coins

    return min_coins


target = 53
coins = [1, 5, 10, 25]
print(recursive_coin_dynamic(target, coins, [0]*(target+1)))
