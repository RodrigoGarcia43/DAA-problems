# input
# positions : int list (lamps positions)
# costs : int list (lamps costs)
# init : initial position of Fito

global_best = [1000000000000000000]


def turn_of(positions, costs, init, turned_of=None, actual_cost=-1, way=[], best=0):
    global global_best
    way_ = []

    n = len(positions)

    if turned_of == None:
        turned_of = []
        for _ in range(0, n):
            turned_of.append(False)

    turned_of[init] = True
    way_ = way.copy()
    way_.append(init)

    if best > global_best[0]:
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
        if best < global_best[0]:
            global_best[0] = best
        return 0, way_

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

        calculate, way1 = turn_of(
            positions, costs, right, turned_of, actual_cost - costs[right], way1, best)

        best -= actual_cost * \
            abs(positions[init] - positions[right])

        calculate_right = actual_cost * \
            abs(positions[init] - positions[right]) + calculate
    else:
        calculate_right = 1000000000000000000000000000

    if not (left == None):
        best += actual_cost * \
            abs(positions[init] - positions[left])

        calculate, way2 = turn_of(
            positions, costs, left, turned_of, actual_cost - costs[left], way2, best)

        best -= actual_cost * \
            abs(positions[init] - positions[left])

        calculate_left = actual_cost * \
            abs(positions[init] - positions[left]) + calculate
    else:
        calculate_left = 1000000000000000000000000000

    turned_of[init] = False
    if calculate_right > calculate_left:
        return calculate_left, way2
    else:
        return calculate_right, way1


def call(positions, costs, init):
    global global_best
    global_best[0] = 1000000000000000000000
    return turn_of(positions, costs, init)
