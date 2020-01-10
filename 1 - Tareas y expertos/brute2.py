min = [100000000000]
t = []


def analize(result, m, n, capacities, tasks, costs, k):

    max = 0
    cost = 0
    count = [0] * m

    for i in range(len(tasks)):
        if capacities[result[i]] < tasks[i]:
            return
        count[result[i]] += 1
        if count[result[i]] > max:
            max = count[result[i]]

    for i in range(len(count)):
        if count[i]:
            cost += costs[i]
            if cost > k:
                return
    if max < min[0]:
        min[0] = max


def get_array(x):
    result = [0] * x
    for i in range(x):
        result[i] = i
    return result


def var_rep(a, variation, pos, m, capacities, tasks, costs, k, n):
    if pos == len(variation):
        analize(variation, m, n, capacities, tasks, costs, k)
        return
    for i in range(len(a)):
        variation[pos] = a[i]
        var_rep(
            a, variation, pos + 1, m, capacities, tasks, costs, k, n)


def generate_all(capacities, costs, tasks, k):
    n = len(tasks)
    m = len(capacities)
    exp = get_array(m)
    result = [0] * n

    min[0] = 100000000000

    var_rep(
        exp, result, 0, m, capacities, tasks, costs, k, n)

    if min[0] == 100000000000:
        return 0
    return min[0]
