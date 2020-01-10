import random


def generator():
    test = "test"
    for i in range(0, 10000):
        aux = test + str(i)
        f = open("tests/" + aux, "w")

        n = random.randint(1, 10)
        m = random.randint(1, n)
        delivers = []
        times = []
        family = []

        for _ in range(0, n):
            valid = True
            deliver = random.randint(0, 40)
            if deliver == 0:
                deliver += 1
            for item in delivers:
                if item == deliver:
                    valid = False
            if valid:

                time = random.randint(0, deliver)
                if time > 2:
                    time -= 1
                if time == 0:
                    time += 1
                delivers.append(deliver)
                times.append(time)

        for _ in range(0, m):
            valid = True
            ma = max(delivers)
            family_day = (random.randint(1, ma))
            for item in delivers:
                if item == family_day:
                    valid = False

            for item in family:
                if item == family_day:
                    valid = False

            if valid:
                family.append(family_day)

        delivers.sort()
        family.sort()

        print(delivers, file=f)
        print(times, file=f)
        print(family, file=f)

        f.close()


generator()
