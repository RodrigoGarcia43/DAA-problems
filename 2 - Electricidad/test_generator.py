import random


def generator():
    test = "test"
    for i in range(0, 10000):
        aux = test + str(i)
        f = open("tests/" + aux, "w")

        n = random.randint(1, 20)
        pos = []
        cost = []

        for _ in range(0, n):
            newpos = random.randint(0, 1000)
            for i in range(len(pos)):
                if newpos == pos[i]:
                    newpos = random.randint(0, 1000)
                    i = 0

            pos.append(newpos)
            cost.append(random.randint(0, 1000))

        pos.sort()
        init = random.randint(1, n)
        if (not n == 0):
            init = init - 1
        print(pos, file=f)
        print(cost, file=f)
        print(init, file=f)

        f.close()


generator()
