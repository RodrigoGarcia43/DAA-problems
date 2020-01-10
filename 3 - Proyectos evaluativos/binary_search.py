import itertools


def getsets(n, k):
    return itertools.combinations(range(n), k)


def f1(projects, k):

    sets = getsets(len(projects), k)
    for comb in sets:
        days = -1
        b = False
        for i in comb:
            days += (projects[i][1] + 1)
            if days > projects[i][0]:
                b = True
            if b:

                break
        if b:
            continue
        if days <= (projects[comb[-1]][0] + 1):

            return len(comb)

    return 0


def binarySearch(projects, fiestas):
    lo = 1
    hi = len(projects)
    solve = 0
    for p in projects:
        c = 0
        for f in fiestas:
            if f <= p[0]:
                c += 1
        p[0] -= c
    while(lo <= hi):
        m = int((lo + hi)/2)
        x = f1(projects, m)
        solve = max(solve, x)
        if x > 0:
            lo = m + 1
        else:
            hi = m - 1

    return solve
