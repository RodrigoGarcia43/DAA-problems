import sys
from math import modf

# return the minimal amount of days for a group of scientifics_ to solve a group od tasks


def calculate_days(scientifics, tasks):
    scientifics_ = scientifics.copy()

    scientifics_.sort()
    tasks_ = tasks.copy()
    tasks_.sort()
    tasks_.append(-1)
    n = len(tasks_)
    m = len(scientifics_)

    # Invalid distribution of scientifics_
    if m == 0 or scientifics_[m-1] < tasks_[n-2]:
        return -1

    if m == 1:
        return n - 1

    mark = 0
    local_group = [0, 0, 0, 0, 0]  # tasks_, scientifics_, quocient, rest, help
    groups = []

    for i in range(0, n):

        if(tasks_[i] > scientifics_[mark] or tasks_[i] == -1):

            while (mark < m and (tasks_[i] > scientifics_[mark] or tasks_[i] == -1)):
                local_group[1] += 1
                mark += 1

            groups.append(local_group)
            local_group = [0, 0, 0, 0, 0]
        local_group[0] += 1

    count = len(groups) - 1

    change = False
    while (True):    # principal loop
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


# cap = [35, 33, 7, 37, 23, 35]
# tasks = [17, 5, 9, 10, 13, 12, 15]
# print(calculate_days(cap, tasks))
