from binary_search import binarySearch as bs

c = [0]
best = []


def copy(mask):
    if len(best) == 0:
        for i in mask:
            best.append(i)
    else:
        for i in range(len(mask)):
            best[i] = mask[i]


def RepletCurrent(current, familyDay):
    for i in range(0, len(familyDay)):
        current[familyDay[i]] = True


def Find(k, projects):
    for i in range(len(projects)):
        if projects[i][0] == k:
            return i
        if projects[i][0] > k:
            break
    return -1


def RepletX(x, tuple, lastMark):
    count = tuple[1]
    for i in range(lastMark, tuple[0]):
        if x[i]:
            continue
        count -= 1
        x[i] = True
        if count == 0:
            return i
    return lastMark


def IsPossible(count, current, mask, projects):
    x = [False] * len(current)
    x = current.copy()
    take = 0
    lastMark = 1

    for i in range(1, len(current)):
        if count == 0:
            break
        if not current[i]:
            take += 1
            continue
        posProject = Find(i, projects)
        if posProject == -1:
            continue
        if take < projects[posProject][1]:
            return False
        lastMark = RepletX(x, projects[posProject], lastMark)
        take -= projects[posProject][1]
        count -= 1
    return True


def Solve_(N, projects, current, mask, count):
    if N == count:
        if IsPossible(count, current, mask, projects) and count > c[0]:
            c[0] = count
            copy(mask)
        return
    for i in range(len(mask)):
        if mask[i]:
            continue
        mask[i] = True
        current[projects[i][0]] = True
        Solve_(N, projects, current, mask, count + 1)
        current[projects[i][0]] = False
        mask[i] = False


def Solve(projects, familyDay):
    for i in range(len(projects)):
        projects[i][0] += 1
    for i in range(len(familyDay)):
        familyDay[i] += 1
    # asumiendo que los proyectos se encuentren en orden
    current = [False] * (projects[-1][0] + 1)
    RepletCurrent(current, familyDay)
    mask = [False] * len(projects)
    c[0] = 0
    best.clear()
    for i in range(1, len(mask) + 1):
        Solve_(i, projects, current, mask, 0)
    # print(best)
    return c[0]

# p = [[13,1]]
# f = [4]
# # m = [False, True, True, False]
# # c = [False] * 24
# # c[1] = True
# # c[10] = True
# # c[12] = True
# # c[19] = True
# # print(IsPossible(2, c, m, p))


# projects = [[1, 13], [2, 2], [5, 3], [10, 1], [
#     13, 7], [19, 2], [20, 1], [25, 1], [30, 28]]
# family = [14, 22]
# print(Solve(projects, family))
