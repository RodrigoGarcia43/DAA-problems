import random


def generator():
    test = "test"
    for i in range(0, 10000):
        aux = test + str(i)
        f = open("tests/" + aux, "w")

        n = random.randint(1, 7)
        m = random.randint(1, 7)

        scientifics = []
        tasks = []
        costs = []
        k = 0

        for _ in range(0, n):
            newtask = random.randint(1, 50)
            scientifics.append(newtask)
            newcost = random.randint(1, 50)
            costs.append(newcost)

        for _ in range(0, m):
            newscient = random.randint(1, 50)
            tasks.append(newscient)

        newk = random.randint(10, 100)
        k = newk

        print(scientifics, file=f)
        print(costs, file=f)
        print(tasks, file=f)
        print(k, file=f)

        f.close()


generator()
