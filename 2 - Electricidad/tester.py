from brute_1 import turn_of as brute_turn_solve
from brute_1_upgraded import call as brute_turn_upgraded_solve
from greedy import turn_of as greedy_turn_solve


# print(f.read())


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
    positions = read_file_line(f)
    costs = read_file_line(f)
    init = read_file_line(f)[0]
    f.close()

    # you can test the following codes

    brute_turn_sol, brute_turn_way = brute_turn_solve(positions, costs, init)

    brute_turn_upgraded_sol, brute_turn_upgraded_way = brute_turn_upgraded_solve(
        positions, costs, init)

    # => this make some mistakes, find it on the pdf

    # greedy_turn_sol, greedy_turn_way = greedy_turn_solve(
    # positions, costs, init)

    count = 0
    if not (brute_turn_upgraded_sol == brute_turn_sol):
        count += 1
        print("ERROR at " + aux)
        print("BRUTE SOLUTION = " + str(brute_turn_upgraded_sol))
        print(brute_turn_upgraded_way)
        print("brute_turn SOLUTION = " + str(brute_turn_sol))
        print(brute_turn_way)

    else:
        print("SUCCES at " + aux)

    print("++++++++++++++ found " + str(count) + " errors")
