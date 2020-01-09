from brute_1 import turn_of as brute_turn
from greedy import turn_of as greedy_turn


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
for i in range(0, 500):
    aux = test + str(i)
    f = open("tests/" + aux, "r")
    positions = read_file_line(f)
    costs = read_file_line(f)
    init = read_file_line(f)[0]
    f.close()

    # print(aux)
    # print(positions)
    # print(costs)
    # print(init)
    # print("##################################")

    brute_sol, brute_way = brute_turn(positions, costs, init)
    greedy_sol, greedy_way = greedy_turn(positions, costs, init)

    if not (brute_sol == greedy_sol):
        print("ERROR at " + aux)
        print("BRUTE SOLUTION = " + str(brute_sol))
        print(brute_way)
        print("GREEDY SOLUTION = " + str(greedy_sol))
        print(greedy_way)

    else:
        print("SUCCES at " + aux)
