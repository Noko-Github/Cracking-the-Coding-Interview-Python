def count_ways(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        count = count_ways(n-1, memo) + count_ways(n-2,
                                                   memo) + count_ways(n-3, memo)
        memo[n] = count
        return count


n = 39
memo = {}
print(count_ways(n, memo))
