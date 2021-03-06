import sys

# input :
# projects : int tuple list (deliver and cost for projects)
# family days : int list (days occuped)


def optimize_projects(projects, family_days):
    _projects = []
    projects.sort()
    family_days.sort()
    n = len(projects)
    family_count = 0
    projects_count = 0
    disp = 0
    local_proyect = [0, 0, 0, 0]  # spended, pending, total cost, flag

    for i in range(0, projects[n-1][0] + 1):

        if(family_count < len(family_days)):
            if(i == family_days[family_count]):
                family_count += 1
                continue

        if(projects[projects_count][0] == i):

            if(projects[projects_count][1] <= disp):

                local_proyect[0] = projects[projects_count][1] + 1
                local_proyect[3] = 1
                local_proyect[1] = 0
                local_proyect[2] = projects[projects_count][1]
                disp -= projects[projects_count][1]
                _projects.append(local_proyect)
                local_proyect = [0, 0, 0, 0]

            elif (projects[projects_count][1] <= i):

                local_proyect[0] = disp
                local_proyect[1] = projects[projects_count][1] - disp
                local_proyect[2] = projects[projects_count][1]
                disp = 0
                _projects.append(local_proyect)

                local_proyect = [0, 0, 0, 0]
            else:
                disp += 1
            projects_count += 1

        else:
            disp = disp + 1

    n = len(_projects)
    for _ in range(0, 2):

        for i in range(0, n):

            pend = order(_projects, i + 1)
            possible = _projects[i][0]

            if len(pend) >= 2:
                poss = False
                amount = 0
                for k in range(0, len(pend)):

                    possible -= pend[k]
                    if (not possible < 0):
                        amount += pend[k]

                    if(possible <= 0):

                        if(possible == 0):
                            if (k >= 1):
                                upgrade = k
                                poss = True
                                if look_fordward(_projects, i, amount, upgrade):
                                    poss = False
                            else:
                                break
                        elif(possible < 0):
                            if(k >= 2):
                                upgrade = k - 1
                                poss = True
                                if look_fordward(_projects, i, amount, upgrade):
                                    poss = False
                                else:
                                    break
                        break

                    if(k == len(pend) - 1):
                        upgrade = k
                        poss = True
                        if look_fordward(_projects, i, amount, upgrade):
                            poss = False

            else:
                poss = False

            if(poss or _projects[i][0] <= _projects[i][2] and i < n-1):

                if(_projects[i][3] == 0):
                    _projects[i][3] = 1
                    _projects[i][0] += 1
                j = i + 1
                gived = 0
                while(_projects[i][0] > 0 and j < n):

                    if(_projects[j][1] == 0):
                        j += 1
                        continue

                    temp = _projects[j][0]
                    if(_projects[i][0] >= (_projects[j][2] - temp)):
                        _projects[j][0] = _projects[j][2] + 1
                        _projects[j][3] = 1
                        _projects[j][1] = 0
                        _projects[i][0] -= (_projects[j][2] - temp)
                        gived += (_projects[j][2] - temp)
                    else:
                        _projects[j][0] += _projects[i][0]
                        _projects[j][1] -= _projects[i][0]
                        gived += _projects[i][0]
                        _projects[i][0] = 0
                    j += 1

                _projects[i][1] += gived

    result = 0
    for item in _projects:
        if item[1] == 0:
            result += 1

    return result


def order(projects, k):
    pend = []
    for i in range(k, len(projects)):
        if projects[i][1] > 0:
            pend.append(projects[i][1])

    pend.sort()

    return pend


def look_fordward(projects, index, amount, k):
    for i in range(index + 1, len(projects)):

        temp = amount
        a = projects[i][0]
        if(projects[i][3] == 0):
            a += 1

        if (a >= amount):

            pend = order(projects, i + 1)

            if len(pend) >= 2:

                for j in range(0, len(pend)):
                    temp -= pend[j]

                    if(temp == 0):
                        if(j >= k):

                            return True
                        else:
                            break
                    if(temp < 0):
                        if(j-1 >= k):
                            return True
                        else:
                            break

                if(j >= k and temp >= 0):
                    return True
    return False
