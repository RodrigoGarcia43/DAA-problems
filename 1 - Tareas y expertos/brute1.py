from calculate_days import calculate_days
import itertools

def analize(comb, costs, scientifics, tasks, k):
    count = 0
    cap = []

    for i in range(0, len(comb)):
        cap.append(scientifics[comb[i]])
        count += costs[comb[i]]
    if count <= k:

        a = calculate_days(cap, tasks)

        if a == -1:
            return 10000000000000000
        return a

    return 10000000000000000


def solve(scientifics, costs, tasks, k):
    global minimal
    minimal = 10000000000000000
    for i in range(1, len(scientifics)+1):

        result = itertools.combinations(range(len(scientifics)), i)
        for r in result:
            x = analize(r, costs, scientifics, tasks, k)
            minimal = min(minimal, x)

    if (minimal == 10000000000000000):
        return 0
    return minimal


minimal = 10000000000000000




