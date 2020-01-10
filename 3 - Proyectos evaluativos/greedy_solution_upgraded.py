import heapq


def solve(projects, party):

    disp = []
    cost = []
    delivery = []
    for p in projects:
        delivery.append(p[0] - 0)
        cost.append(p[1])
        disp.append(p[0])
    ptr = 0
    for i in party:
        ptr = 0
        for e in delivery:
            if i < e:
                disp[ptr] -= 1
            ptr += 1

    orden = []
    for i in range(0, len(cost)):
        orden.append((delivery[i], i))
    orden.sort()

    solution = 0
    mont = 0
    heap = []
    heap.append(0)
    heapq._heapify_max(heap)

    for _, i in orden:
        current_disp = disp[i] - mont
        max_proj = heapq.nlargest(1, heap)
        if current_disp >= cost[i]:
            solution += 1
            mont += (cost[i] + 1)
            heapq.heappush(heap, cost[i])
        elif cost[i] < max_proj[0]:
            mont -= max_proj[0] + 1
            mont += (cost[i] + 1)
            heapq.heappop(heap)
            heapq.heappush(heap, cost[i])
    return solution


projects = [[23, 21], [26, 11], [29, 10], [30, 12], [36, 5], [39, 9]]
family = [24, 27]
print(solve(projects, family))
