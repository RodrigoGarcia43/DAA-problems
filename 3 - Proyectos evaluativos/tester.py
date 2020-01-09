from brute import Solve as brute_solve
from binary_search import binarySearch as binary_solve
from solution1 import optimize_projects as solution1_solve
from solution2 import solve as solution2_solve


def read_file_line(f):
    a = f.readline()
    a = a.replace('[', '')
    a = a.replace(']', '')
    a = a.replace(' ', '')
    a = a.split(',')
    a[len(a) - 1] = a[len(a) - 1].replace('\n', '')
    b = []
    if not (a[0] == ''):
        for item in a:
            b.append(int(item))
    return(b)


count = 0
count_ = 0
test = "test"
for i in range(0, 10000):
    aux = test + str(i)
    f = open("tests/" + aux, "r")
    delivers = read_file_line(f)
    times = read_file_line(f)
    family = read_file_line(f)
    f.close()

    # projects = []
    # for i in range(len(delivers)):
    #     projects.append([delivers[i], times[i]])

    projects = []
    projects1 = []
    for i in range(len(delivers)):
        projects.append([delivers[i] - 0, times[i] - 0])
        projects1.append([delivers[i] - 0, times[i] - 0])
    # print('before----------------------')
    # print(projects)

    solution1_sol = solution1_solve(projects, family)

    binary_sol = binary_solve(projects1, family)

    if not (solution1_sol == binary_sol):
        count += 1
        print("ERROR at " + aux)
        print(projects1)
        print("binary SOLUTION = " + str(binary_sol))
        print(projects)
        print(family)
        print("solution1 SOLUTION = " + str(solution1_sol))

        # if(abs(binary_sol-solution1_sol) > 1):
        #     count_ += 1

    else:
        print("SUCCESS at " + aux)

print("++++++++++++++ found " + str(count) + " errors")
# print("++++++++++++++ found " + str(count_) + " errors geater than 1")
