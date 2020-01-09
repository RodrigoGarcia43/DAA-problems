import sys

# input
# positions : int list (lamps positions)
# costs : int list (lamps costs)
# init : initial position of Fito

count = 0


def turn_of(positions, costs, k):
    way = []
    n = len(positions)
    turned_of = [False] * n
    turned_of[k] = True
    way.append(k)
    on = n-1
    sum = 0

    actual_cost = 0
    for i in range(0, n):
        if turned_of[i] == False:
            actual_cost += costs[i]

    while on > 0:

        best = 0
        best_position = 0
        for i in range(0, n):
            if turned_of[i] == True:
                continue

            distance = abs(positions[i] - positions[k])
            calculate = costs[i] / distance
            # print(i, calculate, distance)
            if calculate > best:
                best = calculate
                best_position = i

        if best_position > k:
            while not k == best_position:
                step_distance = abs(positions[k] - positions[k+1])
                sum = sum + step_distance * actual_cost
                k = k + 1
                if turned_of[k] == False:
                    turned_of[k] = True
                    way.append(k)
                    on = on - 1
                    actual_cost = actual_cost - costs[k]

        else:
            while not k == best_position:
                step_distance = abs(positions[k] - positions[k-1])
                sum = sum + step_distance * actual_cost
                k = k - 1
                if turned_of[k] == False:
                    turned_of[k] = True
                    way.append(k)
                    on = on - 1
                    actual_cost = actual_cost - costs[k]

    return sum, way


# tests
positions = [1, 2, 3, 4, 7, 8, 10, 25, 27, 200]
costs = [10, 1, 15, 1, 10, 2, 5, 1, 100, 50]
init = 5
result, way = turn_of(positions, costs, init)
print(result)
print(way)
