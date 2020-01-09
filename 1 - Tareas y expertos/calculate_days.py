import sys
from math import modf

# return the minimal amount of days for a group of scientifics to solve a group od tasks


def calculate_days(scientifics, tasks):
    scientifics.sort()
    tasks.sort()
    tasks.append(-1)
    n = len(tasks)
    m = len(scientifics)

    if scientifics[m-1] < tasks[n-2]:  # Invalid distribution of scientifics
        return -1

    if m == 1:
        return n - 1

    mark = 0
    # tasks, scientifics, quocient, rest, help
    local_group = [0, 0, 0, 0, 0]
    groups = []

    for i in range(0, n):

        if(tasks[i] > scientifics[mark] or tasks[i] == -1):

            while (mark < m and (tasks[i] > scientifics[mark] or tasks[i] == -1)):
                local_group[1] += 1
                mark += 1

            groups.append(local_group)
            local_group = [0, 0, 0, 0, 0]
        local_group[0] += 1

    count = len(groups) - 1

    change = False
    while (True):
        if count == len(groups)-1:
            if (groups[count][0] > groups[count][1]):
                groups[count][2] = modf(groups[count][0] / groups[count][1])[1]

                rest = groups[count][0] % groups[count][1]

                if rest > 0:
                    groups[count][3] = groups[count][1] - rest
                    groups[count][2] += 1

            else:
                groups[count][2] = 1
                groups[count][3] = groups[count][1] - groups[count][0]

            count -= 1
            if count < 0:
                break
            continue

        if((groups[count][0] - groups[count+1][3] -
                (groups[count+1][1] * groups[count+1][4])) > groups[count][1]):

            q = modf((groups[count][0] - groups[count + 1][3] -
                      (groups[count+1][1] * groups[count+1][4])) / groups[count][1])[1]

            rest = (groups[count][0] - groups[count + 1][3] -
                    (groups[count+1][1] * groups[count+1][4])) % groups[count][1]

            groups[count][2] = q

            if rest > 0:
                groups[count][3] = groups[count][1] - rest
                groups[count][2] += 1

        else:
            groups[count][2] = 1
            groups[count][3] = groups[count][1] - (groups[count][0] - groups[count+1][3] -
                                                   (groups[count+1][1] * groups[count+1][4]))

        if ((groups[count][2] + groups[count][4]) > (groups[count+1][2] + groups[count+1][4])):
            change = True
            groups[count+1][4] += 1

        count -= 1

        if(count < 0):

            if change:
                change = False
                count = count = len(groups) - 1
            else:
                break

    return groups[len(groups)-1][2] + groups[len(groups)-1][4]
