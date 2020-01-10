from calculate_days import calculate_days as c_days


def FindBest(dp, n, k):
    best = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if best == 0 and dp[i][j] > 0:
                best = dp[i][j]
            elif dp[i][j] != 0 and best > dp[i][j]:
                best = dp[i][j]
    return best


def Analize(newSet, c):
    newSet.sort()
    newSet.reverse()

    if len(newSet) > len(c):
        newSet = newSet[0:len(c)]

    reason = 0
    if len(c) % len(newSet) == 0:
        reason = int(len(c) / len(newSet))
    else:
        reason = int(len(c) / len(newSet)) + 1

    # predicado
    for k in range(reason, len(c) + 1):
        posExp = 0
        take = 0
        for i in range(len(c)):
            if c[i] > newSet[posExp]:
                break
            if i == len(c) - 1:
                return k
            if (i - take + 1) % k == 0:
                take = i + 1
                posExp += 1

    return 0


def Knapsack(d, k0, c, k):
    c.sort()
    c.reverse()

    n = len(d)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    exp = [[[]] * (k + 1) for _ in range(n + 1)]

    c.sort()
    c.reverse()

    for i in range(1, n + 1):
        ki = k0[i - 1]
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            exp[i][j] = exp[i - 1][j].copy()

            if j >= ki:
                exp[i][j] = exp[i - 1][j - ki].copy()
                exp[i][j].append(d[i - 1])

                x = Analize(exp[i][j], c)
                if dp[i - 1][j - ki] == 0:
                    dp[i][j] = x
                elif x < dp[i - 1][j - ki]:
                    dp[i][j] = x

    return FindBest(dp, n, k)
