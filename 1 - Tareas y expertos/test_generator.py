import random


def generator():
    # positions = []
    # costs = []
    # inits = []
    test = "test"
    for i in range(0, 1000):
        aux = test + str(i)
        f = open("tests/" + aux, "w")

        n = random.randint(1, 7)
        m = random.randint(1, 7)

        scientifics = []
        tasks = []

        for _ in range(0, n):
            newtask = random.randint(1, 50)
            scientifics.append(newtask)

        for _ in range(0, m):
            newscient = random.randint(1, 50)
            tasks.append(newscient)

        print(scientifics, file=f)
        print(tasks, file=f)

        f.close()

    # return positions, costs, inits


generator()
