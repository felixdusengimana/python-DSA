changes = {}


def coin_change(amount, coins):
    min_coins = amount

    if amount in coins:
        return 1

    for i in [c for c in coins if c <= amount]:
        num_coins = 1 + coin_change(amount - i, coins)
        if num_coins < min_coins:
            min_coins = num_coins

    return min_coins


print(coin_change(15, [1, 15, 13]))
