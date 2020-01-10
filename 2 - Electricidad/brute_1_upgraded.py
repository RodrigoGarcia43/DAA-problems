# input
# positions : int list (lamps positions)
# costs : int list (lamps costs)
# init : initial position of Fito


def turn_of(positions, costs, init, turned_of=None, actual_cost=-1, way=[], best=0, global_best=1000000000000000000):
    way_ = []

    n = len(positions)

    if turned_of == None:
        turned_of = []
        for _ in range(0, n):
            turned_of.append(False)

    turned_of[init] = True
    way_ = way.copy()
    way_.append(init)

    if best >= global_best:
        turned_of[init] = False
        return 0, way_

    right = None
    left = None

    for i in range(init, n):
        if not turned_of[i]:
            right = i
            break

    for i in range(init, -1, -1):
        if not turned_of[i]:
            left = i
            break

    if (right == None and left == None):
        turned_of[init] = False
        if best < global_best:
            global_best = best
        return 0, way_, global_best

    if actual_cost == -1:
        actual_cost = 0
        for i in range(0, n):
            if(not turned_of[i]):
                actual_cost = actual_cost + costs[i]

    way1 = way_.copy()
    way2 = way_.copy()

    if not (right == None):
        best += actual_cost * \
            abs(positions[init] - positions[right])

        calculate, way1, global_best = turn_of(
            positions, costs, right, turned_of, actual_cost - costs[right], way1, best, global_best)

        calculate_right = actual_cost * \
            abs(positions[init] - positions[right]) + calculate
    else:
        calculate_right = 1000000000000000000000000000

    if not (left == None):
        best += actual_cost * \
            abs(positions[init] - positions[left])

        calculate, way2, global_best = turn_of(
            positions, costs, left, turned_of, actual_cost - costs[left], way2, best, global_best)

        calculate_left = actual_cost * \
            abs(positions[init] - positions[left]) + calculate
    else:
        calculate_left = 1000000000000000000000000000

    turned_of[init] = False
    if calculate_right > calculate_left:
        return calculate_left, way2, global_best
    else:
        return calculate_right, way1, global_best


# tests
# positions = [4, 28, 30, 47, 199, 293, 20000, 50000]
# costs = [124, 1253, 132, 532, 124, 634, 124, 6234]
# init = 5
# result, way = turn_of(positions, costs, init)
# print(result)
# print(way)

# total_sum = 0
# check = 0
# pos = 0
# n = len(positions)
# for i in range(1, n):
#     total_sum += costs[way[i]]
# for i in range(1, n):
#     check += total_sum * abs(positions[way[pos]] - positions[way[i]])
#     total_sum -= costs[way[i]]

#     pos = i
# print(check)
