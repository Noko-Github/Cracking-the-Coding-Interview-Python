import math


def make_change(amount, coins, index, map):
    if map[amount][index]:
        return map[amount][index]

    if index >= (len(coins)-1):
        return 1

    counts = 0
    for i in range(math.floor(amount/coins[index]+1)):
        counts += make_change(amount - coins[index]*i, coins, index+1, map)

    return counts


coins = [5, 1]
amount = 10
index = 0
map = [[None] * (len(coins)+1) for i in range(amount+1)]
counts = make_change(amount, coins, index, map)
print(counts)
