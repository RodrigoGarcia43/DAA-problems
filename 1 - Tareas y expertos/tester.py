from brute1 import solve as brute1_solve
from brute2 import generate_all as brute2_solve
from knapsack import Knapsack as knapsack_solve


def read_file_line(f):
    a = f.readline()
    a = a.replace('[', '')
    a = a.replace(']', '')
    a = a.replace(' ', '')
    a = a.split(',')
    a[len(a) - 1] = a[len(a) - 1].replace('\n', '')
    b = []
    for item in a:
        b.append(int(item))
    return(b)


test = "test"
for i in range(0, 10000):
    aux = test + str(i)
    f = open("tests/" + aux, "r")
    capacities = read_file_line(f)
    costs = read_file_line(f)
    tasks = read_file_line(f)
    k = read_file_line(f)
    f.close()

    # you can test the following codes

    brute1_sol = brute1_solve(capacities, costs, tasks, k[0])
    knapsack_sol = knapsack_solve(capacities, costs, tasks, k[0])
    # brute2_sol = brute2_solve(capacities, costs, tasks, k[0])

    count = 0
    if not (brute1_sol == knapsack_sol):
        count += 1
        print("ERROR at " + aux)
        print("first SOLUTION = " + str(brute1_sol))
        print("second SOLUTION = " + str(knapsack_sol))

    else:
        print("SUCCES at " + aux)

    print("Found " + str(count) + " errors")
