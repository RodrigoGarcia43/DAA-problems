from brute import Solve as brute_solve
from binary_search import binarySearch as binary_solve
from solution1 import optimize_projects as solution1_solve
from greedy_solution import solve as greedy_solve
from greedy_solution_upgraded import solve as greedy_upgraded_solve


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

    hollydays = []
    hollydays1 = []

    projects = []
    projects1 = []

    for i in range(len(family)):
        hollydays.append(family[i] - 0)
        hollydays1.append(family[i] - 0)

    for i in range(len(delivers)):
        projects.append([delivers[i] - 0, times[i] - 0])
        projects1.append([delivers[i] - 0, times[i] - 0])

    greedy_upgraded_sol = greedy_upgraded_solve(projects1, hollydays)
    greedy_sol = greedy_solve(projects, hollydays1)

    # this one have an implementation error that we coudn't found
    # we know is an error on the implementation, becouse the idea is similar to the normal greedy
    # All this is explained on the pdf
    # binary_sol = binary_solve(projects1, family)

    # => those make some mistakes, find it on the pdf
    # brute_sol = brute_solve(projects1, family)
    # solution1_upgraded_sol = solution1_upgraded_solve(projects1, family)

    if not (greedy_sol == greedy_upgraded_sol):
        count += 1
        print("ERROR at " + aux)
        print(projects1)
        print("greedy_upgraded SOLUTION = " + str(greedy_upgraded_sol))
        print(projects)
        print(family)
        print("greedy SOLUTION = " + str(greedy_sol))

    else:
        print("SUCCESS at " + aux)

print("++++++++++++++ found " + str(count) + " errors")
