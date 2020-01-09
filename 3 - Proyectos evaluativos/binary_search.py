import itertools


def getsets(n, k):
    return itertools.combinations(range(n), k)


def f1(projects, k):

    sets = getsets(len(projects), k)
    # toret = False
    for comb in sets:
        # print(comb)
        days = -1
        # add = 0
        b = False
        for i in comb:
            days += (projects[i][1] + 1)
        #    print('days: ' + str(days))
            if days > projects[i][0]:
                b = True
            if b:
             #    print('combination')
             #    print(comb)
                break
        if b:
            continue
        if days <= (projects[comb[-1]][0] + 1):
            # print(projects)
            # print(days)
            # print(comb)
            return len(comb)

    return 0


def binarySearch(projects, fiestas):
    lo = 1
    hi = len(projects)
    solve = 0
    # print(projects)
    for p in projects:
        c = 0
        for f in fiestas:
            if f <= p[0]:
                c += 1
        p[0] -= c
    # print(projects)
    while(lo <= hi):
        m = int((lo + hi)/2)
        # print(m)
        x = f1(projects, m)
        solve = max(solve, x)
        if x > 0:
            # solve = max(solve, m)
            lo = m + 1
        else:
            hi = m - 1

    return solve


# projects = [[1,1], [8,6]]

# family = [2]
# [5, 15, 17, 18, 25, 29]
# [11, 2, 21, 12, 2, 5]
# [14, 16, 22, 23, 27, 28]
# print(binarySearch(projects, family))
