# input
# positions : int list (lamps positions)
# costs : int list (lamps costs)
# init : initial position of Fito

count = 0


def turn_of(positions, costs, k, matched=[], actual_cost=-1, way=[]):
    n = len(positions)
    global count

    if matched == []:
        for _ in range(0, n):
            count = count + 1
            matched.append(0)
    matched[k] = 1

    right = None
    left = None

    for i in range(k, n):
        count = count + 1

        if not matched[i]:
            right = i
            break

    for i in range(k, -1, -1):
        count = count + 1

        if not matched[i]:
            left = i
            break

    if (right == None and left == None):
        matched[k] = 0
        way_ = way.copy()
        return 0, way_

    if actual_cost == -1:
        actual_cost = 0
        for i in range(0, n):
            if(matched[i] == 0):
                actual_cost = actual_cost + costs[i]

    if (not right == None):
        way1 = way.copy()
        calculate, way1 = turn_of(
            positions, costs, right, matched, actual_cost - costs[right], way1)
        calculate_right = actual_cost * \
            abs(positions[init] - positions[right]) + calculate
    else:
        result = 0
        last_left = -1
        for i in range(0, k):

            if (matched[i] == 0):
                last_left = i
                break
        while not k == last_left:
            step_distance = abs(positions[k] - positions[k-1])
            result = result + step_distance * actual_cost
            k = k - 1
            if matched[k] == 0:
                matched[k] = 1
                way1.append(k)
                actual_cost = actual_cost - costs[k]
        return result, way1

    if (not left == None):
        way2 = way.copy()
        calculate, way2 = turn_of(
            positions, costs, left, matched, actual_cost - costs[left], way2)
        calculate_left = actual_cost * \
            abs(positions[init] - positions[left]) + calculate
    else:
        result = 0
        last_right = -1
        for i in range(0, k):

            count = count + 1

            if (matched[i] == 0):
                last_right = i
                break
        while not k == last_right:
            step_distance = abs(positions[k] - positions[k+1])
            result = result + step_distance * actual_cost
            k = k + 1
            if matched[k] == 0:
                matched[k] = 1
                way2.append(k)
                actual_cost = actual_cost - costs[k]
        return result, way2

    matched[init] = 0
    if calculate_right > calculate_left:
        return calculate_left, way2
    else:
        return calculate_right, way1


# tests
positions = [1, 2, 3, 4, 7, 8, 10, 25, 27, 30, 200, 270]
costs = [10, 1, 15, 1, 10, 2, 5, 1, 100, 28, 2, 76]
init = 5
result, way = turn_of(positions, costs, init)
print(result)
print(way)
