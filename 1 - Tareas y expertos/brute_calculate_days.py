def solve(scientifics, tasks):
    min = [1000000000]
    scientifics.sort()
    tasks.sort()
    # Invalid distribution of scientifics
    if scientifics[len(scientifics)-1] < tasks[len(tasks)-1]:
        return -1

    def analize(result, m, capacities, tasks):
        max = 0
        count = [0] * m
        for i in range(n):
            if capacities[result[i]] < tasks[i]:
                return
            count[result[i]] += 1
            if count[result[i]] > max:
                max = count[result[i]]

        if max < min[0]:
            min[0] = max

    def get_array(x):
        result = [0] * x
        for i in range(x):
            result[i] = i
        return result

    def Var_rep(a, variacion, pos, m, capacities, tasks):
        if pos == len(variacion):
            analize(variacion, m, capacities, tasks)
            return
        for i in range(len(a)):
            variacion[pos] = a[i]
            Var_rep(
                a, variacion, pos + 1, m, capacities, tasks)

    def generate_all(m, n, capacities, tasks):
        exp = get_array(m)
        result = [0] * n

        Var_rep(exp, result, 0, m, capacities, tasks)

    m = len(scientifics)
    n = len(tasks)

    generate_all(m, n, scientifics, tasks)
    return(min[0])
