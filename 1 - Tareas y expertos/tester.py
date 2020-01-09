from brute_calculate_days import solve as brute_solve
from calculate_days import calculate_days as efficient_solve


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
for i in range(0, 1000):
    aux = test + str(i)
    f = open("tests/" + aux, "r")
    scientifics = read_file_line(f)
    tasks = read_file_line(f)
    f.close()

    brute_sol = brute_solve(scientifics, tasks)
    greedy_sol = efficient_solve(scientifics, tasks)

    if not (brute_sol == greedy_sol):
        print("ERROR at " + aux)
        print("BRUTE SOLUTION = " + str(brute_sol))
        print("EFFICIENT SOLUTION = " + str(greedy_sol))
        print(" ")

    else:
        print("SUCCES at " + aux)
        print(" ")
