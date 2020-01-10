route = []


def is_project_not_taken(p, mp, k, l):
    for i in range(k):
        if not mp[i]:
            if p[i][0] == l:
                return True
            if p[i][0] > l:
                return False
    return False


def is_possible(m, mp, p, k):
    # si es posible colocar el proyecto kesimo en m
    c = 0
    for i in range(1, p[k][0]):
        if m[i]:
            continue
        if is_project_not_taken(p, mp, k, i):
            # print("llegue" + str(i))
            continue
        c += 1
    return c >= p[k][1]


def RepletM(m, mp, p, k):
    # relleno los dias de p[k] en m
    c = 0
    for i in range(1, p[k][0]):
        if m[i]:
            continue
        if not is_project_not_taken(p, mp, k, i):
            c += 1
            m[i] = True
        if c == p[k][1]:
            break
    m[p[k][0]] = True


def repletm_(m, mp, p, k, c, d):
    # rellenar m tomando  c dias free y d dias de proyectos que no se cojieron
    c0 = c
    for i in range(1, p[k][0]):
        if m[i]:
            continue
        if not is_project_not_taken(p, mp, k, i):
            c0 -= 1
            m[i] = True
        if c0 == 0:
            break
    d0 = 0
    for i in range(1, p[k][0]):
        if m[i]:
            continue
        if is_project_not_taken(p, mp, k, i):
            d0 += 1
            m[i] = True
        if c + d0 == p[k][1]:
            break

    for i in range(k):
        if d0 == 0:
            break
        if not mp[i]:
            mp[i] = True
            d0 -= 1

    m[p[k][0]] = True


def days_free(m, mp, p, k):
    # cantidad de dias libres hasta el dia p[k][0]
    d = 0
    for i in range(1, p[k][0]):
        if not m[i] and not is_project_not_taken(p, mp, k, i):
            d += 1
    return d


def days_projects_take(mp, k):
    # cuantos proyectos no se han marcado hasta el dia p[k][0]
    d = 0
    for i in range(k):
        if not mp[i]:
            d += 1
    return d


def max_days_projects(mp, p, k):
    # cual es el proyecto que escogi que tenga mayor cantidad de dias
    max0 = 0
    t = 0
    for i in range(len(route)):
        if p[route[i]][1] > max0:
            max0 = p[route[i]][1]
            t = route[i]

    return t, max0


def contains(route, p, day):
    for i in range(len(route)):
        if p[route[i]][0] == day:
            return True
    return False


def quit_mark(m, p, count, k):
    # coloco los primeras count posiciones en False
    for i in range(1, p[k][0]):
        if contains(route, p, i) or not m[i]:
            continue
        m[i] = False
        count -= 1
        if count == 0:
            break


def solve(p, f):
    for i in range(len(p)):
        p[i][0] += 1
    for i in range(len(f)):
        f[i] += 1

    route.clear()

    m = [False] * (p[-1][0] + 1)
    for i in range(len(f)):
        m[f[i]] = True

    mp = [False] * len(p)

    count = 0

    for i in range(len(p)):
        if is_possible(m, mp, p, i):
            count += 1
            mp[i] = True
            route.append(i)
            RepletM(m, mp, p, i)
        else:
            c = days_free(m, mp, p, i)
            d = days_projects_take(mp, i)
            if c + d >= p[i][1]:

                count += 1
                mp[i] = True
                route.append(i)
                repletm_(m, mp, p, i, c, d)
            else:
                proj, maxDays = max_days_projects(mp, p, i)
                if maxDays > p[i][1]:

                    quit_mark(m, p, maxDays - p[i][1], i)
                    mp[proj] = False
                    mp[i] = True
                    route.append(i)
                    route.remove(proj)
                    m[p[proj][0]] = False
                    m[p[i][0]] = True

    return count
